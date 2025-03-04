import joblib
import numpy as np

class SpamDetector:
    def __init__(self, vectorizer_path, model_path):
        self.vectorizer = joblib.load(vectorizer_path)
        self.model = joblib.load(model_path)
    
    def predict(self, email_text):
        # Transform the input text using the TF-IDF vectorizer
        email_vector = self.vectorizer.transform([email_text])
        
        # Predict using the trained model
        prediction = self.model.predict(email_vector)
        probability = self.model.predict_proba(email_vector)[0][1]
        
        # Invert the prediction (1 becomes 0, 0 becomes 1)
        inverted_prediction = 1 - prediction[0]
        
        return {
            'is_spam': bool(inverted_prediction),
            'spam_probability': float(probability)
        }