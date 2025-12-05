from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')

@app.route("/emotionDetector", methods=["GET", "POST"])
def get_emotion():
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)