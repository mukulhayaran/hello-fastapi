from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

classifier = pipeline("sentiment-analysis")

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API"}

@app.post("/predict")
def predict(input: TextInput):
    result = classifier(input.text)
    return {"label": result[0]["label"], "score": result[0]["score"]}