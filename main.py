from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import sqlite3

app = FastAPI()

classifier = pipeline("sentiment-analysis")

# Database setup
def init_db():
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            label TEXT,
            score REAL
        )
    """)
    conn.commit()
    conn.close()

init_db()

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Sentiment Analysis API"}

@app.post("/predict")
def predict(input: TextInput):
    result = classifier(input.text)
    label = result[0]["label"]
    score = result[0]["score"]
    
    # Save to database
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO predictions (text, label, score) VALUES (?, ?, ?)",
        (input.text, label, score)
    )
    conn.commit()
    conn.close()
    
    return {"label": label, "score": score}

@app.get("/history")
def history():
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT text, label, score FROM predictions")
    rows = cursor.fetchall()
    conn.close()
    return [{"text": r[0], "label": r[1], "score": r[2]} for r in rows]