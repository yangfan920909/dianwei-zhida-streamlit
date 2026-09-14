from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="电维智答 · 变电站故障助手",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML_PATH = Path(__file__).with_name("index.html")
html = HTML_PATH.read_text(encoding="utf-8")

# The original project is a self-contained HTML/CSS/JavaScript prototype.
# Streamlit provides the public hosting shell while the iframe preserves the
# existing interactions and responsive layout.
components.html(html, height=1100, scrolling=True)
