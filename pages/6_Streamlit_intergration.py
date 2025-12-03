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
<h3>US7 — Run ETL Automatically on Streamlit Startup</h3>

<p>
    As a user, I want the ETL pipeline to run automatically when the Streamlit application starts,
    so that the displayed data is always up-to-date and fully processed.
</p>

<p><strong>Acceptance Criteria</strong></p>
<ul>
    <li>ETL pipeline executes once per session using Streamlit caching</li>
    <li>Meaningful and readable error messages shown if ETL fails</li>
    <li>The cleaned dataset is made available globally throughout the app</li>
</ul>
</div>
    """,
    unsafe_allow_html=True,
)
