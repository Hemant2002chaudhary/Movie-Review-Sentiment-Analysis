import streamlit as st
from textblob import TextBlob
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop = set(stopwords.words('english'))

def clean_text(text):
    if not text:
        return ""
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    text = ' '.join([word for word in text.split() if word not in stop])
    return text

def classify(polarity):
    if polarity > 0:
        return "Positive 😊"
    elif polarity < 0:
        return "Negative 😠"
    else:
        return "Neutral 😐"

st.title('📝 Sentiment Checker')
review = st.text_area('Paste a review and click Analyze')

if st.button('Analyze'):
    cleaned = clean_text(review)
    polarity = TextBlob(cleaned).sentiment.polarity
    sentiment = classify(polarity)
    st.subheader("Sentiment:")
    st.write(sentiment)
    st.write(f"Polarity score: {polarity:.3f}")
