import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, ROOT)


print(">>> PYTHON PATH:", sys.path)

import streamlit as st
from src.graph import build_graph  # IMPORTANT: now works because ROOT is set first

graph = build_graph()

st.title("Agentic AI – Multi-Agent System")

user_input = st.text_input("Enter your message:")

if user_input:
    state = {"task": user_input}
    response = graph["respond"](user_input)

    st.write("### Response:")
    st.write(response)


