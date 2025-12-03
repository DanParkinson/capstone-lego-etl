import streamlit as st
import pandas as pd

st.set_page_config(page_title="Choice of Data", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("The Analytics")

st.subheader("Epic 5 — Data Exploration & Visualisation")

# Two user stories → two cards in two columns
col1, col2 = st.columns([1, 1])


# ----------------------------------------
# US8 — Display Cleaned Dataset
# ----------------------------------------
with col1:
    st.markdown(
        """
<div class="card">
<h3>US8 — Display Cleaned Dataset</h3>

<p>
    As a user, I want to preview the cleaned LEGO data,
    so that I can verify the pipeline output directly within the Streamlit UI.
</p>

<p><strong>Acceptance Criteria</strong></p>
<ul>
    <li>A preview of the cleaned DataFrame is visible (e.g., head or sample)</li>
    <li>Displayed columns match the fully processed dataset</li>
    <li>Preview loads without any noticeable performance issues</li>
</ul>
</div>
        """,
        unsafe_allow_html=True,
    )


# ----------------------------------------
# US10 — Provide Visual Insights Through Charts
# ----------------------------------------
with col2:
    st.markdown(
        """
<div class="card">
<h3>US9 — Provide Visual Insights Through Charts</h3>

<p>
    As a user, I want interactive charts showing LEGO trends,
    so that I can explore and understand the cleaned dataset quickly and visually.
</p>

<p><strong>Acceptance Criteria</strong></p>
<ul>
    <li>At least three interactive charts are implemented</li>
    <li>Sidebar filters dynamically update all charts</li>
    <li>Empty filter conditions display a friendly fallback message</li>
</ul>
</div>
        """,
        unsafe_allow_html=True,
    )
