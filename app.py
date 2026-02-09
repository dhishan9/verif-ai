from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
import string
import os

app = Flask(__name__)
CORS(app) # Allows your HTML file to talk to this Python script

# --- 1. THE CLEANING FUNCTION ---
# This must match the one used in train_model.py
def wordopt(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub("\\W"," ",text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

# --- 2. LOAD THE TRAINED MODEL ---
# Make sure 'model.pkl' is in the same folder as this script
try:
    with open('model.pkl', 'rb') as f:
        vectorizer, model = pickle.load(f)
    print("Model and Vectorizer loaded successfully!")
except FileNotFoundError:
    print("Error: model.pkl not found. Please run train_model.py first.")

# --- 3. THE VERIFY ROUTE ---
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    raw_text = data.get('text', '')

    if not raw_text:
        return jsonify({"prediction": "No text provided", "confidence": 0})

    # Clean the input text
    clean_text = [wordopt(raw_text)]

    # Transform text using the loaded vectorizer
    tfidf_input = vectorizer.transform(clean_text)
    
    # Predict (0 = Fake, 1 = Real)
    prediction = model.predict(tfidf_input)[0]
    
    # Calculate Confidence
    # decision_function gives the distance from the threshold
    score = model.decision_function(tfidf_input)[0]
    
    # Normalize score to a 0-100 scale for UI
    confidence = min(99, int(abs(score) * 100))
    if confidence < 50: confidence += 30 # Basic scaling for better UX

    if prediction == 1:
        result = "Likely Credible"
    else:
        result = "High Probability of Fake News"

    return jsonify({
        "prediction": result,
        "confidence": confidence
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
