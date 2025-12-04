import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from src.data_access.app_cache_all_tables import get_tables

st.set_page_config(page_title="Choice of Data", layout="wide")

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("The Analytics")

st.subheader("Epic 5 — Data Exploration & Visualisation")

tables = get_tables()

products_df = tables["products"]
descriptions_df = tables["product_descriptions"]
themes_df = tables["themes"]
countries_df = tables["countries"]
reviews_df = tables["reviews"]
listings_df = tables["product_listings"]

col1, col2 = st.columns([1, 1])

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
</ul>
</div>
        """,
        unsafe_allow_html=True,
    )

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
    <li>At least three charts are implemented</li>
    <li>Empty filter conditions display a friendly fallback message</li>
</ul>
</div>
        """,
        unsafe_allow_html=True,
    )

# General KPIs - col1
total_products = products_df["prod_id"].nunique()
total_countries = countries_df["country_id"].nunique()
total_reviews = listings_df["num_reviews"].sum()

# Global Averge ratings - col2
avg_star = listings_df["star_rating"].mean()
avg_value = listings_df["val_star_rating"].mean()
avg_play = listings_df["play_star_rating"].mean()

# Country KPIs - col3
country_interaction_stats = (
    listings_df.groupby("country_id", as_index=False)
    .agg(total_reviews=("num_reviews", "sum"), avg_star=("star_rating", "mean"))
    .merge(countries_df, on="country_id")
)

highest_rated_country = country_interaction_stats.sort_values(
    "avg_star", ascending=False
).iloc[0]

lowest_rated_country = country_interaction_stats.sort_values(
    "avg_star", ascending=True
).iloc[0]

most_reviewed_country = country_interaction_stats.sort_values(
    "total_reviews", ascending=False
).iloc[0]

least_reviewed_country = country_interaction_stats.sort_values(
    "total_reviews", ascending=True
).iloc[0]

st.markdown("---")
st.subheader("KPIs")

kpi_col1, kpi_col2, kpi_col3 = st.columns(3, vertical_alignment="top")

with kpi_col1:
    st.markdown(
        f"""
        <div class="card">
            <h3>General KPIs</h3>
            <p>Total Products: {total_products}</p>
            <p>Total Countries: {total_countries}</p>
            <p>Total Reviews: {total_reviews}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi_col2:
    st.markdown(
        f"""
        <div class="card">
            <h3>Global Ratings</h3>
            <p>Average Star Rating: {avg_star:.2f}</p>
            <p>Average Value Rating: {avg_value:.2f}</p>
            <p>Average Play Rating: {avg_play:.2f}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with kpi_col3:
    st.markdown(
        f"""
        <div class="card">
            <h3>Country Ratings</h3>
            <p><strong>Highest Rated:</strong> {highest_rated_country['country_name']}
                {highest_rated_country['avg_star']:.2f}</p>
            <p> Lowest Rated: {lowest_rated_country['country_name']}
                {lowest_rated_country['avg_star']:.2f}</p>
            <p>Most Reviews: {most_reviewed_country['country_name']}
                {most_reviewed_country['total_reviews']}</p>
            <p>Least Reviews: {least_reviewed_country['country_name']}
                {least_reviewed_country['total_reviews']}</p>

        </div>
        """,
        unsafe_allow_html=True,
    )

product_stats = (
    listings_df.groupby("prod_id", as_index=False)
    .agg(
        average_stars=("star_rating", "mean"),
        average_play=("play_star_rating", "mean"),
        average_value=("val_star_rating", "mean"),
        total_reviews=("num_reviews", "sum"),
    )
    .merge(products_df[["prod_id", "set_name"]], on="prod_id")
)

top_5_products_rating = product_stats.sort_values(
    ["average_stars", "total_reviews"], ascending=[False, False]
).head(5)

bottom_5_products_rating = product_stats.sort_values(
    ["average_stars", "total_reviews"], ascending=[True, False]
).head(5)

top_5_value = product_stats.sort_values(
    ["average_value", "total_reviews"], ascending=[False, False]
).head(5)

bottom_5_value = product_stats.sort_values(
    ["average_value", "total_reviews"], ascending=[True, False]
).head(5)

top_5_play = product_stats.sort_values(
    ["average_play", "total_reviews"], ascending=[False, False]
).head(5)

bottom_5_play = product_stats.sort_values(
    ["average_play", "total_reviews"], ascending=[True, False]
).head(5)

prod_col1, prod_col2, prod_col3 = st.columns(3, vertical_alignment="top")

with prod_col1:
    # bar chart - product star
    comparison_ratings = pd.concat(
        [
            top_5_products_rating.assign(group="Top 5"),
            bottom_5_products_rating.assign(group="Bottom 5"),
        ],
        ignore_index=True,
    )
    st.markdown("### Top vs Bottom Products – Star Rating")

    base = alt.Chart(comparison_ratings).encode(
        y=alt.Y("set_name:N", sort="-x", title="Product"),
        x=alt.X("average_stars:Q", title="Average Star Rating"),
        color=alt.Color("group:N", legend=None),
        tooltip=["set_name", "group", "average_stars", "total_reviews"],
    )

    bars = base.mark_bar()

    text = base.mark_text(
        align="left",
        baseline="middle",
        dx=5,
        color="white",
    ).encode(text="total_reviews:Q")

    chart = bars + text

    st.altair_chart(
        chart,
    )

with prod_col2:
    # bar chart - value
    comparison_value = pd.concat(
        [
            top_5_value.assign(group="Top 5"),
            bottom_5_value.assign(group="Bottom 5"),
        ],
        ignore_index=True,
    )
    st.markdown("### Top vs Bottom Products – Value Rating")

    base_val = alt.Chart(comparison_value).encode(
        y=alt.Y("set_name:N", sort="-x", title="Product"),
        x=alt.X("average_value:Q", title="Average Value Rating"),
        color=alt.Color("group:N", legend=None),
        tooltip=["set_name", "group", "average_value", "total_reviews"],
    )

    bars_val = base_val.mark_bar()

    text_val = base_val.mark_text(
        align="left", baseline="middle", dx=5, color="white"
    ).encode(text="total_reviews:Q")

    st.altair_chart(bars_val + text_val)

with prod_col3:
    comparison_play = pd.concat(
        [
            top_5_play.assign(group="Top 5"),
            bottom_5_play.assign(group="Bottom 5"),
        ],
        ignore_index=True,
    )

    st.markdown("### Top vs Bottom Products – Play Rating")

    base_play = alt.Chart(comparison_play).encode(
        y=alt.Y("set_name:N", sort="-x", title="Product"),
        x=alt.X("average_play:Q", title="Average Play Rating"),
        color=alt.Color("group:N", legend=None),
        tooltip=["set_name", "group", "average_play", "total_reviews"],
    )

    bars_play = base_play.mark_bar()

    text_play = base_play.mark_text(
        align="left", baseline="middle", dx=5, color="white"
    ).encode(text="total_reviews:Q")

    st.altair_chart(bars_play + text_play)

country_activity = (
    listings_df.groupby("country_id", as_index=False)
    .agg(
        total_reviews=("num_reviews", "sum"),
        products_reviewed=("prod_id", "nunique"),
        avg_reviews_per_product=("num_reviews", "mean"),
    )
    .merge(countries_df, on="country_id", how="left")[
        ["country", "total_reviews", "products_reviewed", "avg_reviews_per_product"]
    ]
)

top_5_active = country_activity.sort_values("total_reviews", ascending=False).head(5)


bottom_5_active = country_activity.sort_values("total_reviews", ascending=True).head(5)


country_compare_activity = pd.concat(
    [
        top_5_active.assign(group="Top 5 Active"),
        bottom_5_active.assign(group="Bottom 5 Active"),
    ],
    ignore_index=True,
)
section_col1, section_col2 = st.columns([2, 1], vertical_alignment="top")

with section_col1:
    st.markdown("### Country Review Activity (Most vs Least Active)")

    activity_base = alt.Chart(country_compare_activity).encode(
        y=alt.Y("country:N", sort="-x", title="Country"),
        x=alt.X("total_reviews:Q", title="Total Reviews"),
        color=alt.Color("group:N", legend=None),
        tooltip=[
            "country",
            "group",
            "total_reviews",
            "products_reviewed",
            "avg_reviews_per_product",
        ],
    )

    activity_bars = activity_base.mark_bar()

    st.altair_chart(activity_bars)

with section_col2:
    st.markdown(
        """
        <div class="card" style="min-height:300px;">
            <h3>Key Insights</h3>
            <p> Most active countires appear to be USA and Canada</p>
            <p> Potentially shows where LEGO engagement is strongest </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

theme_reviews = (
    listings_df.merge(products_df[["prod_id", "theme_id"]], on="prod_id", how="left")
    .merge(themes_df, on="theme_id", how="left")
    .groupby("theme_name", as_index=False)
    .agg(
        avg_star_rating=("star_rating", "mean"),
        avg_value_rating=("val_star_rating", "mean"),
        avg_play_rating=("play_star_rating", "mean"),
        total_reviews=("num_reviews", "sum"),
        products_in_theme=("prod_id", "nunique"),
    )
)

top_5_themes = theme_reviews.sort_values("avg_star_rating", ascending=False).head(5)

bottom_5_themes = theme_reviews.sort_values("avg_star_rating", ascending=True).head(5)

theme_compare = pd.concat(
    [
        top_5_themes.assign(group="Top 5 Themes"),
        bottom_5_themes.assign(group="Bottom 5 Themes"),
    ],
    ignore_index=True,
)
section_col1, section_col2 = st.columns([2, 1], vertical_alignment="top")

with section_col1:
    st.markdown("### Theme Review Performance (Top vs Bottom Themes)")

    theme_base = alt.Chart(theme_compare).encode(
        y=alt.Y("theme_name:N", sort="-x", title="Theme"),
        x=alt.X("avg_star_rating:Q", title="Average Star Rating"),
        color=alt.Color("group:N", legend=None),
        tooltip=[
            "theme_name",
            "group",
            "avg_star_rating",
            "avg_value_rating",
            "avg_play_rating",
            "total_reviews",
            "products_in_theme",
        ],
    )

    theme_bars = theme_base.mark_bar()

    st.altair_chart(theme_bars)

with section_col2:
    st.markdown(
        """
        <div class="card" style="min-height:300px;">
            <h3>Key Insights</h3>
            <p> Themes show a consistent variance in review.</p>
            <p> Themes show consistent ratings across diffferent review categories</p>
            
            
        </div>
        """,
        unsafe_allow_html=True,
    )

theme_country = (
    listings_df.merge(products_df[["prod_id", "theme_id"]], on="prod_id", how="left")
    .merge(themes_df, on="theme_id", how="left")
    .merge(countries_df, on="country_id", how="left")
    .groupby(["theme_name", "country"], as_index=False)
    .agg(
        avg_star_rating=("star_rating", "mean"),
        avg_value_rating=("val_star_rating", "mean"),
        avg_play_rating=("play_star_rating", "mean"),
        total_reviews=("num_reviews", "sum"),
    )
)

excluded_themes = [
    "Blue's Helicopter Pursuit",
    "T. rex Transport",
    "DC Super Hero Girls",
]
theme_country = theme_country[~theme_country["theme_name"].isin(excluded_themes)]

section_col1, section_col2 = st.columns([2, 1], vertical_alignment="top")

with section_col1:
    st.markdown("### Theme × Country Rating Heatmap")
    st.markdown("This shows how different countries rate different LEGO themes.")

    heatmap = (
        alt.Chart(theme_country)
        .mark_rect()
        .encode(
            x=alt.X(
                "country:N",
                title="Country",
                sort=theme_country["country"].unique().tolist(),
            ),
            y=alt.Y(
                "theme_name:N",
                title="Theme",
                sort=theme_country["theme_name"].unique().tolist(),
            ),
            color=alt.Color(
                "avg_star_rating:Q",
                scale=alt.Scale(scheme="yellowgreenblue"),
                title="Avg Star Rating",
            ),
            tooltip=[
                "theme_name",
                "country",
                "avg_star_rating",
                "avg_value_rating",
                "avg_play_rating",
                "total_reviews",
            ],
        )
    )

    st.altair_chart(heatmap)

with section_col2:
    st.markdown(
        """
        <div class="card">
            <h3>Key Insights</h3>
            <p> Noticable vraitions in theme reviews across different countries.</p>
            <p> Some themes perform consistently well </p>
            <p> This bridges teh gap between global theme performance and product level consistency </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

product_country = (
    listings_df.merge(products_df[["prod_id", "set_name"]], on="prod_id", how="left")
    .groupby(["prod_id", "set_name"], as_index=False)
    .agg(
        avg_star_rating=("star_rating", "mean"),
        avg_value_rating=("val_star_rating", "mean"),
        avg_play_rating=("play_star_rating", "mean"),
        std_star=("star_rating", "std"),
        std_value=("val_star_rating", "std"),
        std_play=("play_star_rating", "std"),
        total_reviews=("num_reviews", "sum"),
    )
)

product_country["consistency_score"] = product_country[
    ["std_star", "std_value", "std_play"]
].mean(axis=1)

consistent_products = product_country[product_country["consistency_score"] == 0]
varying_products = product_country[product_country["consistency_score"] > 0]

most_consistent_varying = varying_products.sort_values(
    "consistency_score", ascending=True
).head(5)

least_consistent = varying_products.sort_values(
    "consistency_score", ascending=False
).head(5)

product_compare_varying = pd.concat(
    [
        most_consistent_varying.assign(group="Most Consistent"),
        least_consistent.assign(group="Least Consistent"),
    ],
    ignore_index=True,
)

section_col1, section_col2 = st.columns([2, 1], vertical_alignment="top")

with section_col1:
    st.markdown(
        "### Product Rating Consistency Across Countries (Excluding Consistent Products)"
    )

    chart = (
        alt.Chart(product_compare_varying)
        .mark_bar()
        .encode(
            y=alt.Y("set_name:N", title="Product", sort="-x"),
            x=alt.X("consistency_score:Q", title="Consistency Score (Std Dev)"),
            color=alt.Color("group:N", legend=None),
            tooltip=[
                "set_name",
                "avg_star_rating",
                "avg_value_rating",
                "avg_play_rating",
                "std_star",
                "std_value",
                "std_play",
                "consistency_score",
                "total_reviews",
            ],
        )
    )

    st.altair_chart(chart)

with section_col2:
    st.markdown(
        """
        <div class="card">
            <h3>Key Insights</h3>
            <p> A standard deviation look at different ratings systems across products, across all countries </p>
            <p> Some products had a high variation which shows inconsitent performance across countries
            <p> However, 90% of the data showed almost 0 std across countires which means that LEGO generally is well accepted by people globally. </p>
            <p/> Reccomendation to re-avaluate the products listed below because they arent recieved well everywhere.  
        </div>
        """,
        unsafe_allow_html=True,
    )
