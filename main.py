from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI()

# Load a publicly available multilingual sentiment analysis model from Cardiff NLP.
classifier = pipeline("sentiment-analysis", model="cardiffnlp/twitter-xlm-roberta-base-sentiment")

# Define request schema
class TextRequest(BaseModel):
    text: str

# Define the prediction endpoint
@app.post("/predict")
async def predict(request: TextRequest):
    result = classifier(request.text)
    return {"result": result}
