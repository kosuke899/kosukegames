import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Kosuke Game", layout="wide")

st.markdown(
    """
    <style>
        .stApp {
            background: #111719;
        }
        .block-container {
            padding-top: 0 !important;
            padding-left: 0 !important;
            padding-right: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
        }
        iframe {
            overflow: hidden !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).resolve().parent / "index.html"

with html_path.open("r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(
    html,
    height=700,
    scrolling=False,
)