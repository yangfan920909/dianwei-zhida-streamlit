from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="电维智答 · 建筑电气运维智能中枢",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML_PATH = Path(__file__).with_name("index.html")
components.html(HTML_PATH.read_text(encoding="utf-8"), height=1420, scrolling=True)
