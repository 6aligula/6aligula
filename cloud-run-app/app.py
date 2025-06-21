from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

# Pre-defined automotive categories
CATEGORIES = [
    "Motor",
    "Chasis",
    "Electric",
    "Mantenimiento",
    "Frenos",
    "Neumaticos",
    "Carroceria",
    "Electronica",
    "Accesorios",
    "Otros"
]

classifier = None


def get_classifier():
    """Lazily load the zero-shot classifier."""
    global classifier
    if classifier is None:
        classifier = pipeline(
            "zero-shot-classification",
            model="valhalla/distilbart-mnli-12-1",
        )
    return classifier

@app.route('/classify', methods=['POST'])
def classify():
    data = request.get_json(force=True)
    text = data.get('description', '')
    if not text:
        return jsonify({'error': 'description is required'}), 400

    clf = get_classifier()
    result = clf(text, CATEGORIES)
    # return the label with highest score
    top_label = result['labels'][0]
    return jsonify({'category': top_label})

@app.route('/')
def index():
    return 'OK'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
