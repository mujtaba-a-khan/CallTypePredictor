# Domain-Driven Design (DDD) Documentation

This document outlines the application of Domain-Driven Design (DDD) principles to the Call Type Predictor project. It includes the identification of domains, the development of a strategic design, and the establishment of relationships between domains based on visual Event Storming and a Core Domain Chart.

## Overview of DDD in the Project

Domain-Driven Design is a framework for designing software that ensures complexity is managed through a focus on the core domain and its logic. For the Call Type Predictor project, DDD was instrumental in segregating different areas of functionality into clear domains, thereby facilitating better design and more manageable codebase.

## Domain Identification

The project was broken down into several key domains, each representing a core area of functionality:

### 1. Data Handling
- **Sub-Domains**: Data Loading, Data Preprocessing
- **Responsibilities**: Managing data inputs, cleaning, and formatting data to be used in model training.

### 2. Model Management
- **Sub-Domains**: Model Training, Model Evaluation
- **Responsibilities**: Developing and refining the SVM model, evaluating model performance to ensure accuracy.

### 3. User Interaction
- **Sub-Domains**: User Input Handling, Result Display
- **Responsibilities**: Managing user inputs through GUI, displaying prediction results.

### 4. Configuration and Deployment
- **Sub-Domains**: System Configuration, Deployment Management
- **Responsibilities**: Handling system configurations, managing deployment processes.

## Strategic Design and Domain Relationships

Following the Event Storming session, strategic designs were developed to illustrate the interactions and dependencies between these domains.

### Event Storming Outcomes

- **Key Events**: 'Data Loaded', 'Model Trained', 'Prediction Made'
- **Commands**: 'Load Data', 'Train Model', 'Predict'
- **Aggregates**: Data Repository, Model Configuration, Prediction Engine


## Relationships Between Domains

The domains interact in a structured manner:

- **Data Handling** feeds processed data into the **Model Management** domain for training and evaluation.
- **Model Management** outputs are used by the **User Interaction** domain to display results based on user queries.
- **Configuration and Deployment** supports all other domains by providing necessary infrastructure and deployment capabilities.

## Using DDD to Guide Development

Applying DDD principles helped align the development process with the project’s strategic goals, ensuring that each domain's complexities were appropriately managed and that the team focused on the most critical areas first.

## Conclusion

The application of Domain-Driven Design principles structured the Call Type Predictor project into manageable, focused domains, each tailored to a specific aspect of the software’s functionality. This approach not only facilitated a more organized development process but also enhanced the scalability and maintainability of the software.

---