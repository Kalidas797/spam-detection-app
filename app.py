from flask import Flask, render_template, request, jsonify
import joblib
import os

app = Flask(__name__)

# Load the trained models
tfidf_vectorizer = joblib.load('tfidf_vectorizer.joblib')
spam_model = joblib.load('spam_detection_model.joblib')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the email text from the request
        email_text = request.form['email_text']
        
        # Transform the text using the loaded TF-IDF vectorizer
        text_tfidf = tfidf_vectorizer.transform([email_text])
        
        # Get prediction and probability
        prediction = spam_model.predict(text_tfidf)[0]
        prob = spam_model.predict_proba(text_tfidf)[0]
        
        # Get the confidence percentage
        confidence = prob[1] if prediction == 1 else prob[0]
        confidence_percentage = round(confidence * 100, 2)
        
        # Convert prediction to human-readable format
        result = 'Spam' if prediction == 1 else 'Not Spam'
        
        return jsonify({
            'status': 'success',
            'prediction': result,
            'confidence': confidence_percentage
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)