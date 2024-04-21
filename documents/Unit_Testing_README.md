# Unit Testing Documentation

This document outlines the unit testing approach used in the Call Type Predictor project, focusing specifically on the `CallTypePredictor` class. It explains the methodologies and tools used to test the functionality and robustness of the model management components.

## Overview of Unit Testing Strategy

Unit testing involves isolating each part of the program and showing that the individual parts are correct. A unit test provides a strict, written contract that the piece of code must satisfy. In the context of the Call Type Predictor project, unit testing primarily ensures that the model's data processing, training, and evaluation components behave as expected under various conditions.

## Testing Framework and Tools

The unit tests were implemented using Python’s `unittest` framework. This framework was chosen for its robustness, ease of integration with Python applications, and support for test automation.

### Key Features of `unittest`:
- **TestCase Class**: Provides a way to organize test code and to run multiple tests together.
- **Assertions**: Methods that check for specific behaviors and conditions.
- **Test Fixtures**: Setup and teardown operations that provide a clean base for each test to run.

## Tests for the `CallTypePredictor` Class

The `CallTypePredictor` class includes several critical functions that were targeted for testing:

### 1. Data Preprocessing
- **Test Objective**: Ensure that the data preprocessing handles various edge cases correctly, such as empty data fields, incorrect formats, and non-string input.
- **Methods Tested**:
  - `data_preprocessor()`: Tests whether the function correctly filters non-usable data and formats the remaining data for further processing.

### 2. Model Training
- **Test Objective**: Verify that the model training function correctly applies the vectorization and training processes using the input data.
- **Methods Tested**:
  - `train_model()`: Checks if the model is properly trained with the specified number of features and maintains the expected accuracy threshold.

### 3. Model Evaluation
- **Test Objective**: Confirm that the model evaluation correctly calculates the model's performance metrics.
- **Methods Tested**:
  - `evaluate_model()`: Ensures accuracy calculations are correct and errors in input data are handled gracefully.

## Example Test Case

Here’s a simplified example of a unit test for the `data_preprocessor` method:

```python
import unittest
from main import CallTypePredictor
import pandas as pd

class TestCallTypePredictor(unittest.TestCase):
    def setUp(self):
        self.model = CallTypePredictor()
        self.sample_data = pd.DataFrame({
            'transcript_text': ['call connected', '', None, 'call missed', 'call missed'],
            'actual_call_connection': ['connected', 'missed', 'missed', None, 'connected']
        })

    def test_data_preprocessor(self):
        # Filtering out records where 'transcript_text' is empty or None
        self.model.data_preprocessor(self.sample_data)
        self.assertEqual(self.model.transcript_text_data_train.shape, (1,))  # Expecting only 1 valid record
        self.assertEqual(self.model.transcript_text_data_test.shape, (1,))
        self.assertEqual(self.model.actual_call_connection_data_train.shape, (1,))
        self.assertEqual(self.model.actual_call_connection_data_test.shape, (1,))

if __name__ == '__main__':
    unittest.main()
```


``` bash
Loaded dataset with shape: (2, 2)
.
----------------------------------------------------------------------
Ran 1 test in 0.003s

OK
```

## Conclusion

Unit tests in the Call Type Predictor project are essential for ensuring that each component of the `CallTypePredictor` class functions correctly under various scenarios. They provide confidence in the model's reliability and accuracy, supporting ongoing development and maintenance efforts.

---
