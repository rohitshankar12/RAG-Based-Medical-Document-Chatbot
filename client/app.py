import sys
from pathlib import Path

import streamlit as st

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from component.upload import render_uploader
from component.history_download import render_history_download
from component.chatui import render_chat

st.set_page_config(page_title="AI Medical Assistant", layout="wide")
st.title("🩺 Medical Assistant Chatbot")

render_uploader()
render_chat()
render_history_download()