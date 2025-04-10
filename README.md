🎬 IMDb Movie Review Sentiment Analyzer

This is a deep learning-based web application that predicts the sentiment (positive or negative) of a movie review using a trained neural network model. Built with TensorFlow and deployed using Streamlit, the app provides real-time sentiment analysis of user input.


🚀 Live Demo
🔗 IMDb Sentiment Analyzer


📌 Features
Input any movie review text

Predicts Positive or Negative sentiment

Displays model confidence score with a visual progress bar

Intuitive UI with Streamlit


🧠 Model Overview
Tokenizer: Keras Tokenizer, fitted on IMDb reviews dataset

Model: Sequential neural network built with:

Embedding layer

LSTM or GRU (or Dense layers if simplified)

Dense output layer with sigmoid activation

Training Data: IMDb Movie Review Dataset (Binary classified)


🧪 Example Usage
💬 Review: "This movie was a thrilling masterpiece!"

✅ Prediction: Positive
📊 Confidence: 95.42%

📦 Dependencies
streamlit

tensorflow

numpy

scikit-learn

pickle (built-in)

