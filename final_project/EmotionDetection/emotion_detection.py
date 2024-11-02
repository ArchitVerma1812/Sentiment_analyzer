import requests
import json

def emotion_detector(text_to_analyse):  
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json=myobj, headers=header)
    formatted_response = json.loads(response.text)  # Convert response text to dictionary
    
    if(response.status_code == 400):
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    else:
        emotion_data = formatted_response.get("emotionPredictions", [{}])[0].get("emotion", {})
        anger_score = emotion_data.get("anger", 0)
        disgust_score = emotion_data.get("disgust", 0)
        fear_score = emotion_data.get("fear", 0)
        joy_score = emotion_data.get("joy", 0)
        sadness_score = emotion_data.get("sadness", 0)
    
    # Find the dominant emotion
        emotion_scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)  # Emotion with the highest score
    
    # Return the output in the specified format
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
