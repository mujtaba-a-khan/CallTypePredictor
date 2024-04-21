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