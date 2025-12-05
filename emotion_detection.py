import requests
import json

def emotion_detector(text_to_analyze):
    # Endpoint URL
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    # Required headers
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    # JSON payload
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    # POST request
    response = requests.post(url, headers=headers, json=payload)
    # Return the text attribute of the response object
    return response.text
