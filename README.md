---
title: Sentiment API
emoji: 🎭
colorFrom: blue
colorTo: green
sdk: docker
app_port: 7860
pinned: false
---

# Sentiment Analysis App

A full-stack NLP web application that analyzes the sentiment of text using a fine-tuned transformer model.

## 🔗 Live Demo
- **Frontend**: https://mukul-sentiment.streamlit.app
- **API**: https://mukulhayaran-sentiment-api.hf.space/docs

## 🛠 Tech Stack
- **Model**: DistilBERT (HuggingFace Transformers)
- **Backend**: FastAPI + SQLite
- **Frontend**: Streamlit
- **Deployment**: Docker + HuggingFace Spaces + Streamlit Cloud

## 🏗 Architecture



```
User → Streamlit Frontend → FastAPI Backend → DistilBERT Model
                                    ↓
                               SQLite DB (logs predictions)
```


## ✨ Features
- Real-time sentiment classification (Positive/Negative)
- Confidence score for each prediction
- Prediction history stored in SQLite database
- REST API with auto-generated Swagger documentation
- Dockerized backend for consistent deployment

## 🚀 Run Locally

**Backend:**
```bash
git clone https://github.com/mukulhayaran/hello-fastapi.git
cd hello-fastapi
pip install -r requirements.txt
uvicorn main:app --reload
```

**Frontend:**
```bash
streamlit run app.py
```

