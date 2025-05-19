from flask import Flask, render_template, request, jsonify
from utils.dream_logic import analyze_sleep, detect_emotion, generate_dream_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    sleep_data = data.get('sleep_data', [])
    journal = data.get('journal', '')

    sleep_summary = analyze_sleep(sleep_data)
    emotion = detect_emotion(journal)
    dream_url = generate_dream_image(emotion)

    return jsonify({
        'sleep_summary': sleep_summary,
        'emotion': emotion,
        'dream_url': dream_url
    })

if __name__ == '__main__':
    app.run(debug=True)
