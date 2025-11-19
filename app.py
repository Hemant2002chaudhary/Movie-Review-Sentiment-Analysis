# app.py
import streamlit as st
from textblob import TextBlob
import re

# Clean text function
def clean_text(text):
    text = re.sub(r'[^A-Za-z0-9\s]+', '', text)
    text = text.lower()
    return text.strip()

# Classify polarity
def classify(polarity):
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

# Streamlit interface
st.title('🧠 Sentiment Checker')
review = st.text_area('Paste your review below:')

if st.button('Analyze'):
    if review.strip() == "":
        st.warning("Please paste a review before analyzing.")
    else:
        cleaned = clean_text(review)
        polarity = TextBlob(cleaned).sentiment.polarity
        sentiment = classify(polarity)
        st.success(f"Sentiment: {sentiment}")
