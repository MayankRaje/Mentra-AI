# Mentra AI

Mentra AI is an AI-powered technical interview preparation assistant.

The project is being built step by step to understand how GenAI applications work in practice using Python, FastAPI, Pydantic, prompt engineering, and LLM integration.

## Current Features

* FastAPI-based backend
* Pydantic request and response validation
* Interview question and candidate-level input
* Dynamic prompt generation
* OpenRouter LLM integration
* Free-model support through OpenRouter
* AI-generated technical interview answers
* Structured LLM responses
* Pydantic validation for LLM output
* Automatic Swagger / OpenAPI documentation

## Current Architecture

```text
Client
  ↓
FastAPI Endpoint
  ↓
Pydantic Request Validation
  ↓
Prompt Generation
  ↓
LLM Service
  ↓
OpenRouter
  ↓
Free LLM
  ↓
Structured JSON Response
  ↓
JSON Parsing
  ↓
Pydantic Response Validation
  ↓
API Response
```

## Project Structure

```text
mentra/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── config.py
│   ├── prompt.py
│   └── llm_service.py
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Tech Stack

* Python
* FastAPI
* Pydantic
* OpenRouter
* OpenAI-compatible Python SDK
* Uvicorn

## Example Usage

Mentra accepts a technical interview question and the target interview level, then generates an interview-oriented answer using an LLM.

### Example Request

```json
{
  "question": "How would you prevent duplicate payment processing in a distributed system when retries and concurrent requests are possible?",
  "level": "SDE-2"
}
```

The request passes through the backend flow:

```text
Request
→ FastAPI
→ Pydantic Request Validation
→ Prompt Generation
→ OpenRouter LLM
→ Structured JSON
→ JSON Parsing
→ Pydantic Response Validation
→ API Response
```

## API Demo

The `/interview-answer` endpoint can be tested directly using FastAPI's Swagger UI.

The API accepts the interview question and candidate level and returns an AI-generated response.

Add your working Swagger screenshot here:

![img.png](img.png)

The screenshot should show the request, `200` status code, and the generated response.

## Environment Configuration

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=openrouter/free
```

Do not commit the `.env` file to GitHub.

Create a `.env.example` file that can safely be committed:

```env
OPENROUTER_API_KEY=your_api_key_here
OPENROUTER_MODEL=openrouter/free
```

## Run Locally

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
uvicorn app.main:app --reload
```

Verify the backend:

```text
http://127.0.0.1:8000
```

Open Swagger:

```text
http://127.0.0.1:8000/docs
```

## Development Progress

### Day 1 — Backend Foundation

* Initialized the FastAPI application
* Added Pydantic request and response models
* Created the `/interview-answer` endpoint
* Tested the request-response flow using Swagger
* Returned a temporary response before connecting an LLM

### Day 2 — LLM Integration

* Added dynamic prompt generation
* Created a separate LLM service layer
* Integrated OpenRouter
* Configured a free LLM model
* Added environment-based API configuration
* Successfully generated real AI interview answers through the API

## What I’m Learning

This project is helping me understand how a GenAI application is built beyond simply calling an LLM API:

* API design with FastAPI
* Input/output validation with Pydantic
* Prompt construction
* External LLM integration
* Environment-based secret management
* Separation of API, configuration, prompt, and LLM service responsibilities

## Next Step

The next iteration will focus on **structured LLM output**.

Instead of returning the complete answer as one string, Mentra will return separate sections such as:

```text
Short Answer
Explanation
Example
Interview Tip
```

This will make the API response easier to consume, validate, and extend in later versions.
