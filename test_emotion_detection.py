import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestingEmotionDetector(unittest.TestCase):
    def test_dominant_emotions(self):
        test_cases = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }
        for statement, expected in test_cases.items():
            result = emotion_detector(statement)
            dominant = result.get("dominant_emotion")
            print(f"Statement: {statement} | Result: {dominant} | Expected: {expected}")
            self.assertEqual(dominant, expected)

if __name__ == '__main__':
    unittest.main()