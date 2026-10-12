import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Kosuke Game", layout="wide")

html_path = Path(__file__).resolve().parent / "index.html"

with html_path.open("r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=900, scrolling=True)