import requests

API_KEY = "YOUR_ELEVENLABS_API_KEY"
VOICE_ID = "YOUR_VOICE_ID"

def speak_text(text):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75}
    }
    response = requests.post(url, headers=headers, json=data)
    with open("output.mp3", "wb") as f:
        f.write(response.content)
    return "output.mp3"