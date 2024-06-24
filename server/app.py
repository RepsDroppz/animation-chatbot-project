from flask import Flask, request, jsonify
from flask_cors import CORS
from animation_chatbot import AnimationChatbot

app = Flask(__name__)
CORS(app)
chatbot = AnimationChatbot()

@app.route('/api/animate', methods=['POST'])
def animate():
    data = request.json
    text = data.get('text', None)
    if text:
        animation = chatbot.create_animation_from_text(text)
    else:
        return jsonify({'error': 'Invalid input'}), 400

    return jsonify({'animation': animation}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
