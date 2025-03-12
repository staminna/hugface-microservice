from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import os

app = FastAPI()

# Define request schema
class GenerateRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 50

# -----------------------------------------------------------------------------
# Model identifier (use lowercase)
# -----------------------------------------------------------------------------
MODEL_ID = "facebook/opt-125m"  # Changed to a publicly available model

# Read the Hugging Face access token from environment variable (if required)
HF_TOKEN = os.environ.get("HF_TOKEN")

# -----------------------------------------------------------------------------
# Load Tokenizer & Model (with authentication if needed)
# -----------------------------------------------------------------------------
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_ID,
    # Removed use_auth_token since we're using a public model
)

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    # Removed use_auth_token
)

# Create a text-generation pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    device_map="auto" if device == "cuda" else None  # Only use device_map with GPU
)

# -----------------------------------------------------------------------------
# FastAPI endpoint
# -----------------------------------------------------------------------------
@app.get("/")
def health_check():
    return {"status": "ok", "model": MODEL_ID}

@app.post("/generate")
def generate_text(request: GenerateRequest):
    outputs = generator(
        request.prompt,
        max_new_tokens=request.max_new_tokens,
        do_sample=True,
        top_p=0.95,
        temperature=0.8
    )
    return {"generated_text": outputs[0]["generated_text"]}
