import tkinter as tk
from tkinter import ttk  # Importing ttk for styled widgets
from tkinter import filedialog, messagebox
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from typing import Annotated, Tuple
from mlflow.models.model import ModelInfo
import mlflow
import threading

# install the required packages
# !pip install matplotlib
# !pip install scikit-learn
# !pip install pandas
# !pip install mlflow

class CallTypePredictor:

    data_processor_return_type = Tuple[
        Annotated[pd.Series, "transcript_text_data_train"],
        Annotated[pd.Series, "transcript_text_data_test"],
        Annotated[pd.Series, "actual_call_connection_data_train"],
        Annotated[pd.Series, "actual_call_connection_data_test"],
    ]

    train_model_return_types = Tuple[Annotated[SVC, "classifier"], Annotated[ModelInfo, "model"], Annotated[TfidfVectorizer, "vectorizer"]]

    def __init__(self):
        self.classifier = None
        self.model = None
        self.vectorizer = None

        self.accuracy = None
        self.test_size = None
        self.random_state = None
        self.max_features = None

        self.transcript_text_data_train = None
        self.transcript_text_data_test = None
        self.actual_call_connection_data_train = None
        self.actual_call_connection_data_test = None

    def data_preprocessor(self, dataset: pd.DataFrame, test_size: float = 0.3, random_state: int = 42) -> data_processor_return_type:
        dataset = dataset[dataset["actual_call_connection"].isin(["connected", "missed"])]
        dataset = dataset[dataset["transcript_text"].notnull()]
        dataset = dataset[dataset["transcript_text"] != ""]
        dataset["transcript_text"] = dataset["transcript_text"].astype(str)

        # Extracting features and labels
        transcript_text_data = dataset["transcript_text"]
        actual_call_connection_data = dataset["actual_call_connection"]

        # Splitting the dataset into training and testing sets & return
        self.transcript_text_data_train, self.transcript_text_data_test, self.actual_call_connection_data_train, self.actual_call_connection_data_test = train_test_split(
            transcript_text_data, actual_call_connection_data, test_size=test_size, random_state=random_state
        )
        print(f"Loaded dataset with shape: {dataset.shape}")

    def train_model(
        self, transcript_text_data_train: pd.Series, actual_call_connection_data_train: pd.Series, random_state: int = 42, max_features: int = 1000
    ) -> train_model_return_types:
        self.vectorizer = TfidfVectorizer(max_features=max_features)
        transcript_text_data_train_vectorized = self.vectorizer.fit_transform(transcript_text_data_train)

        self.classifier = SVC(random_state=random_state)
        self.classifier.fit(transcript_text_data_train_vectorized, actual_call_connection_data_train)
        print(f"Model trained with max_features: {max_features}")
        pipe = Pipeline([("tfidf", self.vectorizer), ("clf", self.classifier)])

        self.model = mlflow.sklearn.log_model(pipe, "model")

    def evaluate_model(
        self,
        classifier: SVC,
        transcript_text_data_test: pd.Series,
        actual_call_connection_data_test: pd.Series,
        vectorizer: TfidfVectorizer,
        random_state: int = 42,
        test_size: float = 0.3,
        max_features: int = 1000,
    ) -> None:
        transcript_text_data_test_vectorized = vectorizer.transform(transcript_text_data_test)
        self.accuracy = classifier.score(transcript_text_data_test_vectorized, actual_call_connection_data_test)

        self.test_size = test_size
        self.random_state = random_state
        self.max_features = max_features

        # Log model parameters
        print(f"Model evaluated with accuracy: {self.accuracy}")
        print(f"test_size: {self.test_size}")
        print(f"random_state: {self.random_state}")
        print(f"max_features: {self.max_features}")


def load_data():
    file_path = filedialog.askopenfilename(title="Select File", filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")))
    if file_path:
        data = pd.read_csv(file_path)
        model.data_preprocessor(
            data
        )
        model.train_model(model.transcript_text_data_train, model.actual_call_connection_data_train)
        model.evaluate_model(
            model.classifier, model.transcript_text_data_test, model.actual_call_connection_data_test, model.vectorizer
        )

        lbl_status.config(text="Model Trained")
        lbl_accuracy.config(text=f"Accuracy: {model.accuracy:.2f}")
        display_plots(model.transcript_text_data_train, model.actual_call_connection_data_train)
    else:
        messagebox.showerror("Error", "No file selected")


model = CallTypePredictor()


def debounce(wait):
    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)
            if hasattr(debounced, '_timer'):
                debounced._timer.cancel()
            debounced._timer = threading.Timer(wait, call_it)
            debounced._timer.start()
        return debounced
    return decorator


@debounce(0.5)
def delayed_predict():
    transcript = txt_transcript.get("1.0", tk.END).strip()
    if transcript:
        prediction = model.classifier.predict(model.vectorizer.transform([transcript]))[0]
        lbl_prediction.config(text=f"Prediction: {prediction}")
    else:
        lbl_prediction.config(text="Prediction: Type something...")


def display_plots(X, y):
    # Preprocess data for plotting
    unique_classes = y.unique()
    colors = {'connected': 'blue', 'missed': 'red'}
    class_counts = y.value_counts()

    # Create a figure with subplots
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))  # Changed to a single row of two plots

    # Plotting class distribution
    axs[0].bar(class_counts.index, class_counts.values, color=[colors[i] for i in class_counts.index])
    axs[0].set_title("Class Distribution")
    axs[0].set_ylabel("Counts")

    # Plotting histogram of the length of transcripts
    transcript_lengths = X.apply(len)
    axs[1].hist(transcript_lengths, bins=20, color='gray')
    axs[1].set_title("Transcript Length Distribution")
    axs[1].set_xlabel("Length of Transcripts")
    axs[1].set_ylabel("Frequency")

    # Display the canvas in the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


# Main application window
window = tk.Tk()
window.title("Call Type Predictor")

# Styling
style = ttk.Style()
style.theme_use('clam')  # You can choose other themes like 'alt', 'default', 'classic', 'vista'

# Use frames to organize sections
frame_train = ttk.Frame(window, padding="10 10 10 10")
frame_train.pack(fill=tk.X, padx=10, pady=5)

frame_predict = ttk.Frame(window, padding="10 10 10 10")
frame_predict.pack(fill=tk.X, padx=10, pady=5)

frame_output = ttk.Frame(window, padding="10 10 10 10")
frame_output.pack(fill=tk.X, padx=10, pady=5)

# Model training components
btn_load = ttk.Button(frame_train, text="Load and Train Model", command=load_data)
btn_load.pack(side=tk.LEFT, expand=True)

lbl_status = ttk.Label(frame_train, text="Status: Not trained")
lbl_status.pack(side=tk.LEFT, expand=True)

# Prediction components
txt_transcript = tk.Text(frame_predict, height=4, wrap='word', font=('Helvetica', 10))
txt_transcript.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)
txt_transcript.bind('<KeyRelease>', lambda event: delayed_predict())

lbl_prediction = ttk.Label(frame_predict, text="Prediction: type something...")
lbl_prediction.pack(side=tk.LEFT, expand=True, padx=10)

# Model details
lbl_accuracy = ttk.Label(frame_output, text="Accuracy: N/A")
lbl_accuracy.pack(side=tk.TOP, pady=10)

# Run the main loop
window.mainloop()