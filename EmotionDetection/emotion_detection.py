import requests
import json

def emotion_detector(text_to_analyse):
    '''
    Detect emotion from text using the Emotion Prediction function in Watson NLP Library
    '''
    # url, header, input json for the Emotion Prediction function in Watson NLP Library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = input_json, headers=header)

    # Parsing the JSON response from the API

    json_response = json.loads(response.text)
    emotion_list = ['anger','disgust','fear','joy','sadness']
    output_dict = {}
    # If the response status code is 200, extract values for output_dict
    if response.status_code == 200:

        highest_score = 0
        dominant_emotion = None
        for e in emotion_list:
            score = json_response['emotionPredictions'][0]['emotion'][e]
            output_dict[e] = score
            if score > highest_score:
                highest_score = score
                dominant_emotion = e
        output_dict['dominant_emotion'] = dominant_emotion
    # If the response status code is 400, set value = None for each output_dict item
    elif response.status_code == 400:
        keys = emotion_list+['dominant_emotion',]
        for k in keys:
            output_dict[k] = None      
    return output_dict

