import streamlit as st
import pandas as pd

st.set_page_config(page_title="Choice of Data", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Further Development Ideas")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown(
        """
<div class="card" style="min-height:420px;">
    <h3>Load Data Into a Database</h3>
    <ul>
        <li>Replace local CSV output with a proper relational database (e.g., PostgreSQL).</li>
        <li>Define clear DDL schemas for fact and dimension tables.</li>
        <li>Migrate the write process to SQLAlchemy or psycopg2 for long-term scalability.</li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
<div class="card" style="min-height:420px;">
    <h3>Break Down Long Descriptions</h3>
    <ul>
        <li>Parse <strong>prod_long_desc</strong> into structured, analytical fields.</li>
        <li>Extract key attributes such as dimensions, features, included items, and model metadata.</li>
        <li>Separate narrative/marketing text from factual product data.</li>
        <li>Store extracted details in a dedicated <code>product_features</code> or <code>product_metadata</code> table.</li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
<div class="card" style="min-height:400px;">
    <h3>Automated & Extensible Transform Process</h3>
    <ul>
        <li>Refactor the transform stage into a fully automated pipeline that can detect column types.</li>
        <li>Introduce dynamic rules based on schemas (e.g., numeric → numeric clean, text → text clean).</li>
        <li>Handle schema drift automatically when new columns appear in future datasets.</li>
        <li>Create a plugin-style architecture where new cleaning rules can be added without editing core code.</li>
        <li>Allow the process to scale to multiple datasets or new LEGO themes with minimal changes.</li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )
