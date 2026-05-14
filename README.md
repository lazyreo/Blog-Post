# Blog Post Streamlit Exercises

This repository contains three small Streamlit example apps demonstrating session state, callback usage, and AI integration for blog creation.

## Files

- `manual_blog_run.py` - A manual blog post creator interface.
  - Click `+ Create` to enter a title, introduction, main body, and conclusion.
  - When all fields are filled, the app displays the completed blog post.
  - Uses `st.session_state` to store `create_new_blog`, `done`, and the blog content.

- `ai_blog_run.py` - An AI-powered blog post generator.
  - Enter a topic and click `Submit` to generate a blog post using Google's Gemini AI.
  - The app streams the AI response and displays the formatted blog post.

- `test.py` - A counter example with callback arguments.
  - Enter an increment value and click `Increment`.
  - The count is stored in `st.session_state.count` and updated with each click.

- `llm_client.py` - A client for interacting with Google's Gemini AI API.

## Requirements

- Python 3.14 or higher
- Dependencies as listed in `pyproject.toml`

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Run

To run the manual blog post creator:

```bash
streamlit run manual_blog_run.py
```

To run the AI blog post generator:

```bash
streamlit run ai_blog_run.py
```

To run the counter example:

```bash
streamlit run test.py
```

## Notes

- `manual_blog_run.py` uses a button callback to switch into blog creation mode.
- `ai_blog_run.py` integrates with Google's Gemini AI for content generation (requires API key in `.env`).
- `test.py` demonstrates passing the current input value to a callback function.
