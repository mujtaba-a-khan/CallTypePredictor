# Metrics Documentation

This document details the metrics collected during the development and testing of the Call Type Predictor project. Metrics play a crucial role in evaluating the performance, efficiency, and accuracy of the model, guiding decisions on future improvements and optimizations.

## Overview of Metrics Used

Metrics in this project were focused on evaluating the machine learning model's performance and the overall data handling efficiency. Here are the key metrics that were tracked:

### 1. Dataset Metrics
- **Dataset Size**: Total number of records and features in the dataset used for training and testing the model.
  - **Value**: 14,521 records, 5 features per record

### 2. Model Training Metrics
- **Max Features**: The maximum number of features used by the TF-IDF vectorizer to transform text data.
  - **Value**: 1,000 features
- **Random State**: A fixed random state ensures that the model's training and testing phases are reproducible.
  - **Value**: 42

### 3. Model Performance Metrics
- **Accuracy**: Measures the percentage of correctly predicted instances out of all predictions made.
  - **Value**: 96.42%
- **Test Size**: The proportion of the dataset reserved for testing the model's performance.
  - **Value**: 30% of the dataset

## Importance of Metrics

### Accuracy
- **Importance**: Accuracy is crucial for evaluating the effectiveness of the classification model. A high accuracy rate indicates that the model is performing well in distinguishing between 'connected' and 'missed' calls based on the transcripts.
- **Impact**: The high accuracy achieved (96.42%) validates the model's capability in its predictive tasks, supporting its use in operational settings.

### Dataset Size
- **Importance**: Understanding the size and scope of the dataset helps in assessing the model's robustness and its ability to handle real-world data of similar scales.
- **Impact**: A large dataset ensures that the model is trained on a diverse set of data points, which can enhance its generalizability.

### Max Features
- **Importance**: The number of features considered by the TF-IDF vectorizer affects the complexity and specificity of the feature space for model training.
- **Impact**: Setting max_features to 1000 helps in maintaining a balance between model complexity and training efficiency, ensuring fast and effective training sessions without compromising on performance.

## Conclusion

The metrics gathered throughout the development process have been instrumental in guiding the optimization and validation of the Call Type Predictor. They provide a quantitative basis for assessing the model’s performance and are essential for continuous improvement efforts.

---