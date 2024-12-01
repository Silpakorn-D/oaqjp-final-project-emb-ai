from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        test_cases = {
                        'I am glad this happened':'joy',
                        'I am really mad about this':'anger',
                        'I feel disgusted just hearing about this':'disgust',
                        'I am so sad about this':'sadness',
                        'I am really afraid that this will happen':'fear',
                        }
        for k,v in test_cases.items():
            result = emotion_detector(k)['dominant_emotion']
            self.assertEqual(result, v)
        	
unittest.main()	
	
	
	