import requests
import json

def emotion_detector(text_to_analyse):
    # url, header, input json for the Emotion Prediction function in Watson NLP Library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = input_json, headers=header)

    # Parsing the JSON response from the API

    json_response = json.loads(response.text)
    emotion_list = ['anger','disgust','fear','joy','sadness']
    output_dict = {}
    highest_score = 0
    dominant_emotion = None
    for e in emotion_list:
        score = json_response['emotionPredictions'][0]['emotion'][e]
        output_dict[e] = score
        if score > highest_score:
            highest_score = score
            dominant_emotion = e
    output_dict['dominant_emotion'] = dominant_emotion   
    return output_dict

