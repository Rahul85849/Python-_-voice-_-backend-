from flask import Flask, request, send_file
from gpt_engine import get_explanation
from eleven_tts import speak_text

app = Flask(__name__)

@app.route("/explain", methods=["POST"])
def explain():
    code = request.json['code']
    explanation = get_explanation(code)
    audio_path = speak_text(explanation)
    return send_file(audio_path, mimetype="audio/mpeg")