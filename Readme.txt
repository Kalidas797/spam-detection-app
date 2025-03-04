# Spam Detection Web App

This is a Spam Detection Web App that uses a Machine Learning model to classify emails as Spam or Ham (Not Spam). The web app is hosted on Render and provides a simple interface for users to enter email text and get real-time predictions.

## Live Demo
🔗 [Visit the Web App](https://spam-detection-app-lshp.onrender.com/)

## Features
- Real-time Spam Detection: Enter an email message and get an instant classification.
- Machine Learning Model: Built using scikit-learn with TF-IDF vectorization to process raw text into numerical features for training.
- Dataset Improvements: Enhanced the dataset by balancing spam and ham emails to improve detection accuracy.
- Deployment: Hosted on Render with a Flask backend.

## Model Training and Improvements
This model is based on Siddhardhan’s ML course(https://youtu.be/LcWFedjaR4Q?si=wHdp5ndJNOdFjVMd). While his model performs well, however the original dataset had an imbalance — more ham emails than spam emails, which affected the model’s performance.
 I made modifications such as balancing the dataset to improve spam recall. Below is a comparison of both models.

### Enhancements I Made:
✅ Balanced the dataset (Equal spam & ham emails)
✅ Standardized the text data for better consistency
✅ Improved Recall & Accuracy for spam detection

### Model Performance Comparison
| Metric                      | My Model | Siddhardhan’s Model | Improvement  |
|-----------------------------|----------|----------------------|--------------|
| Accuracy                | 98%      | 96%                  | ✅ +2%       |
| Precision (Spam)        | 100%     | 100%                 | 🔵 Same (No false positives) |
| Recall (Spam)           | 82%      | 72%                  | ✅ +10%      |
| F1-Score (Spam)         | 90%      | 84%                  | ✅ +6%       |
| False Negatives (Missed Spam) | 27 | 42 | ✅ Reduced False Negatives |

## Technologies Used
- Python
- Flask (For backend API)
- scikit-learn (For ML model)
- Pandas & NumPy (For data processing)
- NLTK (For text preprocessing)
- Render (For deployment)

## Installation & Setup
If you want to run this project locally, follow these steps:

1. Clone this repository:
   ```bash
   git clone https://github.com/Kalidas797/spam-detection-app.git
   cd spam-detection-app
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

## Future Improvements
- Implement Deep Learning models for better accuracy.
- Add User Authentication to save email history.
- Improve UI/UX with better design and interactivity.

## Contributing
Feel free to fork this repo and create a pull request if you want to contribute.

## License
This project is licensed under the MIT License.

---
Made with ❤️ by Kalidas797 🚀

