from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    
    # Generate output string
    emotions = ", ".join([f"'{key}': {value}" for key, value in response.items() if key != "dominant_emotion"])
    dominant_emotion = response["dominant_emotion"]

    output = f"For the given statement, the system response is {emotions}. The dominant emotion is {dominant_emotion}."
    return output

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)