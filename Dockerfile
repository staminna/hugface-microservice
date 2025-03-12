# Use a lightweight Python image
FROM python:3.9-slim

# Create and switch to a working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy our app code
COPY main.py .

# Expose the FastAPI port
EXPOSE 8000

# Run with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
