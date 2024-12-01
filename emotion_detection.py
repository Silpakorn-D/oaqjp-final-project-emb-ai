import requests
def emotion_detector(text_to_analyse):
    # url, header, input json for the Emotion Prediction function in Watson NLP Library
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = json, headers=header)
    return response.text