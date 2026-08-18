# Mentra AI

Day 1 starter project for Mentra AI.

## Project structure

```text
mentra/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── models.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Run locally

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 to verify the API is running.
