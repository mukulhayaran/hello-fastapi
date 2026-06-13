import streamlit as st
import requests

st.title("Sentiment Analysis App")
st.write("Enter a sentence to analyze its sentiment.")

text = st.text_input("Your text here")

if st.button("Analyze"):
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={"text": text}
    )
    result = response.json()
    st.write(f"Label: {result['label']}")
    st.write(f"Confidence: {result['score']:.2f}")