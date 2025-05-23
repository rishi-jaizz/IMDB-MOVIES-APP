# -*- coding: utf-8 -*-
"""imdb_sentiment_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pUqXA2y6epwdMV7lcqrf2rmJWCUDIwK4
"""

import streamlit as st
import numpy as np
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load tokenizer
with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Load trained model
model = tf.keras.models.load_model("sentiment_model.h5")

# Streamlit UI setup
st.set_page_config(page_title="IMDb Sentiment Analyzer", layout="centered")
st.title("🎬 IMDb Movie Review Sentiment Analyzer")
st.write("Enter a movie review below, and the model will predict whether it's positive or negative.")

# Text input from user
user_input = st.text_area("Movie Review:", height=150)

# Prediction logic
if st.button("Analyze Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter a movie review.")
    else:
        # Preprocess text
        sequence = tokenizer.texts_to_sequences([user_input])
        padded = pad_sequences(sequence, maxlen=200)

        # Make prediction
        prediction = model.predict(padded)[0][0]

        # Normalize confidence score for progress bar
        confidence_score = prediction if prediction > 0.5 else 1 - prediction
        confidence_score = max(0.0, min(1.0, float(confidence_score)))  # Ensure it's a Python float between 0 and 1

        # Display sentiment result
        if prediction > 0.5:
            st.success("✅ Positive Review")
        else:
            st.error("❌ Negative Review")

        # Show confidence bar
        st.progress(confidence_score)
        st.write(f"Model confidence: **{confidence_score * 100:.2f}%**")