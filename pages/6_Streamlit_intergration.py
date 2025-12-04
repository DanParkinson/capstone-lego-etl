import streamlit as st
import pandas as pd

st.set_page_config(page_title="Choice of Data", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Loading into Streamlit")
st.subheader("Epic 4 — Streamlit Application")


st.markdown(
    """
<div class="card">
<h3>US7 — Streamlit app loads datasets</h3>

<p>
    As a user, I want a streamlit application that presents data,
    so that I can view analytical insights.
</p>

<p><strong>Acceptance Criteria</strong></p>
<ul>
    <li>ETL pipeline executes once per session using Streamlit caching</li>
</ul>
</div>
    """,
    unsafe_allow_html=True,
)
