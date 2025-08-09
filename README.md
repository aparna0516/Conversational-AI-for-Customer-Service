# AI-Powered Chatbot (Sample Project)

This is a **sample** AI-powered chatbot project you can upload to GitHub.  
It contains a simple Flask backend and a minimal web UI. NLP is done using spaCy similarity matching against example phrases (intents). This is a lightweight starting point — replace the NLP logic with a transformer model, or hook up to OpenAI/HuggingFace for more advanced responses.

## What's included
- `app.py` — Flask REST API for chat.
- `nlp.py` — Minimal intent matcher using spaCy.
- `intents.json` — Sample intents and example phrases.
- `static/index.html` — Simple web chat UI.
- `requirements.txt` — Python dependencies.
- `Dockerfile` — Optional containerization.
- `LICENSE` — MIT license.

## Quick start (local)
1. Create and activate a virtualenv:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open your browser at `http://127.0.0.1:5000`

## Notes & How to extend
- Replace `nlp.py` with a transformer-based intent & response system (HuggingFace/LLMs).
- Add authentication, DB (Postgres), logging, and analytics.
- Integrate escalation logic with ticketing systems (Zendesk, Freshdesk) using their APIs.

## Deploy
Use Docker:
```bash
docker build -t ai-chatbot-sample .
docker run -p 5000:5000 ai-chatbot-sample
```
