# FastAPI Text Generation Microservice

A lightweight microservice that provides text generation capabilities using Hugging Face models via a RESTful API.

## Features

- Simple REST API for text generation
- Uses Hugging Face Transformers for state-of-the-art language models
- Containerized with Docker for easy deployment
- Automatic GPU detection and utilization when available

## Quick Start

### Prerequisites

- Docker

### Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t opt-125m-microservice .
   ```

2. Run the container:
   ```bash
   docker run -p 8001:8000 opt-125m-microservice
   ```
   
   Note: If port 8001 is already in use, you can change it to any available port.

3. The service will be available at `http://localhost:8001`

## API Endpoints

### Health Check

```
GET /
```

Returns the status of the service and the model being used.

Example response:
```json
{
  "status": "ok",
  "model": "facebook/opt-125m"
}
```

### Generate Text

```
POST /generate
```

Request body:
```json
{
  "prompt": "Once upon a time",
  "max_new_tokens": 50
}
```

Parameters:
- `prompt`: The input text to generate from
- `max_new_tokens`: Maximum number of tokens to generate (default: 50)

Example response:
```json
{
  "generated_text": "Once upon a time, there was a young princess who lived in a castle..."
}
```

## Configuration

The service uses the following environment variables:
- None required for the default public model

## Development

### Local Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the service:
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## License

MIT

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Hugging Face Transformers](https://huggingface.co/transformers/)
