from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.post("/predict")
def predict(input: TextInput):
    return {"you_sent": input.text, "length": len(input.text)}
