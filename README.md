# Blog Post Streamlit Apps

This repository contains Streamlit examples for creating blog posts manually and generating blog content with AI.

## Files

- `manual_blog_run.py` - Manual blog creator.
  - Click `+ Create` to enter a title, introduction, main body, and conclusion.
  - When all fields are completed, the app displays the finished blog post.
  - Uses `streamlit.session_state` to manage creation state and stored content.

- `ai_blog_run.py` - AI-powered blog post generator.
  - Enter a topic and click `Submit` to generate a blog post via Google Gemini.
  - Streams the AI-generated text to the app and stores it in session state.
  - Includes a button to export the generated text as `final_doc.pdf`.

- `llm_client.py` - Gemini AI client wrapper.
  - Loads `MY_API_KEY` from the `.env` file and sends requests to the Gemini API.

- `pdf.py` - PDF export helper.
  - Converts generated text into a PDF file saved as `final_doc.pdf`.

## Requirements

- Python 3.14 or higher
- Dependencies as listed in `pyproject.toml`

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

Create a `.env` file in the project root with:

```env
MY_API_KEY=your_google_gemini_api_key
```

## Run

To run the manual blog creator:

```bash
streamlit run manual_blog_run.py
```

To run the AI blog generator:

```bash
streamlit run ai_blog_run.py
```

## Notes

- `manual_blog_run.py` is a simple manual blog builder using Streamlit inputs and session state.
- `ai_blog_run.py` sends user input to Google Gemini and streams the generated blog response.
- `pdf.py` saves the generated AI output as a PDF file.
- `llm_client.py` depends on `dotenv` to load the API key from `.env`.
