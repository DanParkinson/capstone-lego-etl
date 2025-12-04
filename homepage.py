import streamlit as st

st.set_page_config(page_title="LEGO Analytics", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Welcome to my LEGO ETL Pipeline Presentation")

st.write(
    "This project demonstrates the full lifecycle of building a professional, "
    "tested ETL pipeline using real-world LEGO product and review data."
)

st.write("The goal was to design a clear, reliable system that included:")

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown(
        """
        <div class="card">
            <h3>1. A Robust ETL Pipeline</h3>
            <ul>
                <li>Modular ETL structure</li>
                <li>Extensive unit test coverage</li>
                <li>Logging and performance checks</li>
            </ul>
        </div>

        <div class="card">
            <h3>2. Strong Principles</h3>
            <ul>
                <li>Strict separation of concerns</li>
                <li>Reusable, testable functions</li>
                <li>Validation at raw and clean stages</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">
            <h3>3. Preparing Data for Analytics</h3>
            <ul>
                <li>Cleaned numeric + text fields</li>
                <li>Removed duplicates responsibly</li>
                <li>Created relational-style tables</li>
            </ul>
        </div>

        <div class="card">
            <h3>4. Presenting Findings</h3>
            <ul>
                <li>Show improvements made during ETL</li>
                <li>Reveal insights in the dataset</li>
                <li>Outline future enhancements</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="card tall-card">
            <h3>Content Covered:</h3>
            <ul>
                <li><strong>1. Choice of Data</strong></li>
                <li><strong>2. Extraction</strong></li>
                <li><strong>3. Transformation</strong></li>
                <li><strong>4. Loading</strong></li>
                <li><strong>5. Streamlit Integration</strong></li>
                <li><strong>6. Challenges & Takeaways</strong></li>
                <li><strong>7. Future Development</strong></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
