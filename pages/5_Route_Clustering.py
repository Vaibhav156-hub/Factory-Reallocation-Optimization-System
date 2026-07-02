import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Route Clustering",
    layout="wide"
)

# ===================================
# LOAD DATA
# ===================================

df = pd.read_csv("Processed_Nassau_Candy.csv")
cluster = pd.read_csv("Cluster_Summary.csv")

st.title("📍 Route Clustering Dashboard")

st.markdown("""
Analyze shipping routes and cluster performance.
""")

st.markdown("---")

# ===================================
# KPI CARDS
# ===================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Routes",
    len(df)
)

col2.metric(
    "Products",
    df["Product Name"].nunique()
)

col3.metric(
    "Factories",
    df["Origin_Factory"].nunique()
)

st.markdown("---")

# ===================================
# CLUSTER SUMMARY
# ===================================

st.subheader("📋 Cluster Summary")

st.dataframe(
    cluster,
    use_container_width=True
)

st.markdown("---")

# ===================================
# DISTANCE vs LEAD TIME
# ===================================

fig = px.scatter(
    df,
    x="Distance_km",
    y="Lead_Time",
    color="Origin_Factory",
    hover_data=["Product Name"],
    title="Distance vs Lead Time"
)

st.plotly_chart(fig, use_container_width=True)

# ===================================
# FACTORY DISTRIBUTION
# ===================================

fig2 = px.pie(
    df,
    names="Origin_Factory",
    title="Factory Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# ===================================
# PRODUCT DISTRIBUTION
# ===================================

fig3 = px.histogram(
    df,
    x="Division",
    color="Division",
    title="Division Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# ===================================
# DISTANCE DISTRIBUTION
# ===================================

fig4 = px.histogram(
    df,
    x="Distance_km",
    nbins=25,
    title="Shipping Distance Distribution"
)

st.plotly_chart(fig4, use_container_width=True)