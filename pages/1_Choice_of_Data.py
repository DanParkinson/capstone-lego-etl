import streamlit as st
import pandas as pd

st.set_page_config(page_title="LEGO Analytics", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.title("Choice of Data")
st.write(
    """
Understanding the dataset is the first stage of any ETL project.  
For this project, I selected a publicly available **LEGO product and review dataset** from Kaggle.
"""
)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>Why This Dataset?</h3>
            <ul>
                <li>It contains <strong>real-world product data</strong> (names, themes, prices, ages, descriptions).</li>
                <li>Includes <strong>customer review information</strong> from multiple countries.</li>
                <li>Contains enough quality issues to justify a full ETL process:
                    <ul>
                        <li>Mixed data types</li>
                        <li>Inconsistent age formats</li>
                        <li>Missing descriptions</li>
                        <li>Duplicated rows</li>
                        <li>Multiple values packed into single columns</li>
                    </ul>
                </li>
                <li>Ideal for demonstrating a structured, test-driven pipeline.</li>
            </ul>
        </div>

        <div class="card">
            <h3>What the Raw Dataset Looks Like</h3>
            <p>
                The source dataset arrives as <strong>one large CSV file</strong> (~12,000 rows),
                with columns including:
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


with col2:

    html_table = """
    <div class="card">
        <table>
            <tr><td><strong>ages</strong></td><td>6-12</td></tr>
            <tr><td><strong>list_price</strong></td><td>29.99999</td></tr>
            <tr><td><strong>num_reviews</strong></td><td>2.0</td></tr>
            <tr><td><strong>piece_count</strong></td><td>277.0</td></tr>
            <tr><td><strong>play_star_rating</strong></td><td>4.0</td></tr>
            <tr><td><strong>prod_desc</strong></td><td>Catapult into action and take back the eggs from the Piggy Trike!</td></tr>
            <tr><td><strong>prod_id</strong></td><td>75823.0</td></tr>
            <tr><td><strong>prod_long_desc</strong></td>
                <td>Use the staircase catapult to launch Red into the air and race after the piggy...
                </td>
            </tr>
            <tr><td><strong>review_difficulty</strong></td><td>Average</td></tr>
            <tr><td><strong>set_name</strong></td><td>Bird Island Egg Heist</td></tr>
            <tr><td><strong>star_rating</strong></td><td>4.5</td></tr>
            <tr><td><strong>theme_name</strong></td><td>Angry Birds™</td></tr>
            <tr><td><strong>val_star_rating</strong></td><td>4.0</td></tr>
            <tr><td><strong>country</strong></td><td>US</td></tr>
        </table>
    </div>
    """

    st.markdown(html_table, unsafe_allow_html=True)

st.markdown("---")
st.subheader("Issues and Plan")
st.write(
    "Before building the ETL pipeline, it was important to understand what the raw dataset looked like and what issues needed addressing."
)

# Columns
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown(
        """
        <div class="card tall-card">
            <h3>Key Issues Identified in the Raw Data</h3>

        <p><strong>1. Mixed numeric formatting</strong></p>
        <ul>
            <li>Ages stored as inconsistent strings</li>
            <li>Numeric ratings stored as text</li>
        </ul>

        <p><strong>2. Missing and inconsistent text fields</strong></p>
        <ul>
            <li>Many products have no descriptions</li>
            <li>Mixed casing in difficulty ratings</li>
        </ul>

        <p><strong>3. Duplicate rows from multiple reviews</strong></p>
        <ul>
            <li>Repeated <code>prod_id</code> and <code>country</code> combinations</li>
        </ul>

        <p><strong>4. Single-table structure not suited for analysis</strong></p>
        <ul>
            <li>Mixes product attributes, descriptions, themes, and reviews into one table</li>
        </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card tall-card">
            <h3>What We Aim to Do in Cleaning</h3>

        <ul>
            <li>Convert numeric-like fields into true numeric types</li>
            <li>Create standardised age fields (<code>age_min</code>, <code>age_max</code>)</li>
            <li>Clean & normalise all text fields</li>
            <li>Handle missing descriptions intelligently</li>
            <li>Remove duplicate or corrupted rows</li>
        </ul>

        <p>Split the dataset into <strong>six relational tables</strong>:</p>
        <ul>
            <li>products</li>
            <li>product_descriptions</li>
            <li>reviews</li>
            <li>product_listings</li>
            <li>themes</li>
            <li>countries</li>
        </ul>

        </div>
        """,
        unsafe_allow_html=True,
    )
