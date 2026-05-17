# Enhanced Q&A Chatbot

A small Streamlit app that uses LangChain/OpenAI to answer user questions.

## Features
- Streamlit UI with model, temperature and token controls
- Minimal LangChain prompt/chain setup
- Optional LangSmith tracing (disabled by default)

## Requirements
- Python 3.10+
- Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment
Create a `.env` file in the project root with the following variables as needed:

- `OPENAI_API_KEY` — Your OpenAI API key (used to call models). Optional if you paste a key into the Streamlit sidebar at runtime.
- `LANGCHAIN_API_KEY` — (Optional) LangSmith API key for tracing. If missing or invalid, tracing uploads may return 403 but the app will still run.
- `LANGCHAIN_PROJECT` — (Optional) LangSmith project name.
- `LANGCHAIN_TRACING_V2` — Set to `true` only if you want LangSmith tracing enabled and you have a valid `LANGCHAIN_API_KEY`.

Example `.env`:

```dotenv
OPENAI_API_KEY=sk-...
LANGCHAIN_API_KEY=lsv2_...
LANGCHAIN_PROJECT=MyProject
LANGCHAIN_TRACING_V2=true
```

## Run locally

```bash
# from project root
streamlit run app.py
```

Open http://localhost:8501 in your browser. In the sidebar you can paste an `OPENAI_API_KEY` (if not set in `.env`), select a model, and adjust settings.
