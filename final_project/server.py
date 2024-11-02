"""Flask application for emotion detection using NLP.

This application provides an API endpoint to analyze text input 
and detect emotions such as anger, disgust, fear, joy, and sadness. 
It uses an external emotion detection service and returns the 
emotional scores along with the dominant emotion.
"""

from flask import Flask, render_template, request, jsonify # Importing Flask and necessary modules
from EmotionDetection.emotion_detection import emotion_detector # Importing emotion detection module

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main index page."""
    return render_template("index.html")

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Handle emotion detection requests."""
    data = request.get_json()
    text_to_analyse = data.get('textToAnalyze', '').strip()  # Strip to handle extra spaces
    if not text_to_analyse:
        return jsonify({"Error": "No text provided"}), 400  # Return an error if no text is provided

    result = emotion_detector(text_to_analyse)

    # Check if the dominant emotion is None
    if result.get('dominant_emotion') is None:
        return jsonify({"Error": "Invalid text! Please try again!"}), 400

    return jsonify(result)
