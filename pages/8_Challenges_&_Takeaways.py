import streamlit as st
import pandas as pd

st.set_page_config(page_title="Choice of Data", layout="wide")

# Load CSS
with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("Challenges & Takeaways")
st.subheader("Challenges")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown(
        """
<div class="card" style="min-height: 260px;">
    <h3>Planning</h3>
    <ul>
        <li>Designing a plan that is detailed enough to make progress but still adaptable.</li>
        <li>Having full freedom over where and how to store the data.</li>
        <li>Accepting that the plan will change once you start working with the real data.</li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
<div class="card" style="min-height: 260px;">
    <h3>General</h3>
    <ul>
        <li>Figuring out what actually needs cleaning in the dataset.</li>
        <li>Knowing what to test to get good coverage without overdoing it.</li>
        <li>Realising how misleading data can be if you don’t properly inspect it.</li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )


with col3:
    st.markdown(
        """
<div class="card" style="min-height: 260px;">
    <h3>Technical</h3>
    <ul>
        <li>Refactoring functions to be generic, reusable, and easier to maintain.</li>
        <li>Handling the <code>ages</code> column and writing robust regex logic.</li>
        <li>Discovering that “simple” steps (like handling failure paths) need careful thought.</li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )


st.markdown("---")
st.subheader("Takeaways")
col4, col5, col6 = st.columns([1, 1, 1])


with col4:
    st.markdown(
        """
<div class="card" style="min-height: 260px;">
    <h3>Planning</h3>
    <ul>
        <li>Plan first — it saves time and stress later.</li>
        <li>Using sprints is genuinely helpful for structuring the work.</li>
        <li>Plan tests and error handling early, not as an afterthought.</li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )


with col5:
    st.markdown(
        """
<div class="card" style="min-height: 260px;">
    <h3>General</h3>
    <ul>
        <li>It’s not as overwhelming as it first seems once you break it down.</li>
        <li>Don’t rush — slow, deliberate work leads to better outcomes.</li>
        <li>If you’re tired, step away; tired coding usually leads to bad code.</li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )

with col6:
    st.markdown(
        """
<div class="card"style="min-height: 260px;">
    <h3>Technical</h3>
    <ul>
        <li>Reusable functions massively reduce duplication and bugs.</li>
        <li>Separation of concerns makes the codebase easier to reason about.</li>
        <li>Building a logger early pays off across the whole project.</li>
    </ul>
</div>
        """,
        unsafe_allow_html=True,
    )
