from flask import Flask, request, jsonify
import os

import classifier

app = Flask(__name__)

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json(force=True)
    text = data.get('description', '')
    if not text:
        return jsonify({'error': 'description is required'}), 400

    category = classifier.classify_text(text)
    return jsonify({'category': category})

@app.route('/')
def index():
    return 'OK'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
