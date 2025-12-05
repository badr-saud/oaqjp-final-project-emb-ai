"""
server.py

This module runs a Flask web server for the EmotionDetection application.
It exposes a POST endpoint '/emotionDetector' that receives text input
and returns emotion scores along with the dominant emotion.
"""
from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """Rendering the main paga"""
    return render_template('index.html')



@app.route("/emotionDetector", methods=["GET", "POST"])
def get_emotion():
    """Endpoint for making the request to emotion analysis"""
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
