from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import nlp

app = Flask(__name__, static_folder='static', static_url_path='/static')
CORS(app)

# load resources at startup
nlp.load_resources()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json() or {}
    message = data.get('message', '').strip()
    if not message:
        return jsonify({'error': 'empty message'}), 400
    result = nlp.predict_intent(message)
    # simple escalation: if low confidence, instruct escalation
    if result['confidence'] < 0.5:
        return jsonify({
            'message': "I couldn't fully understand. I'm escalating this to a human agent.",
            'intent': result['tag'],
            'confidence': result['confidence'],
            'escalate': True
        })
    return jsonify({
        'message': result['response'],
        'intent': result['tag'],
        'confidence': result['confidence'],
        'escalate': False
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
