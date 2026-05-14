# Blog Post Streamlit Exercises

This repository contains two small Streamlit example apps demonstrating session state and callback usage.

## Files

- `main.py` - A blog post creator interface.
  - Click `+ Create` to enter a title, introduction, main body, and conclusion.
  - When all fields are filled, the app displays the completed blog post.
  - Uses `st.session_state` to store `create_new_blog`, `done`, and the blog content.

- `test.py` - A counter example with callback arguments.
  - Enter an increment value and click `Increment`.
  - The count is stored in `st.session_state.count` and updated with each click.

## Requirements

- Python 3.14 or higher
- Streamlit 1.57.0 or higher

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you do not have `requirements.txt`, install Streamlit directly:

```bash
pip install streamlit
```

## Run

To run the blog post creator:

```bash
streamlit run main.py
```

To run the counter example:

```bash
streamlit run test.py
```

## Notes

- `main.py` uses a button callback to switch into blog creation mode.
- `test.py` demonstrates passing the current input value to a callback function.
