import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Factory Performance",
    layout="wide"
)

# ===============================
# LOAD DATA
# ===============================

factory = pd.read_csv("Factory_Performance.csv")

st.title("🏭 Factory Performance Dashboard")

st.markdown("---")

# ===============================
# KPI CARDS
# ===============================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Factories",
    len(factory)
)

best_factory = factory.loc[
    factory["Average_Profit"].idxmax(),
    "Factory"
]

col2.metric(
    "Best Factory",
    best_factory
)

col3.metric(
    "Average Profit",
    f"${factory['Average_Profit'].mean():.2f}"
)

col4.metric(
    "Average Lead Time",
    f"{factory['Average_Lead_Time'].mean():.2f}"
)

st.markdown("---")

# ===============================
# FACTORY PERFORMANCE TABLE
# ===============================

st.subheader("📋 Factory Summary")

st.dataframe(
    factory,
    use_container_width=True
)

st.markdown("---")

# ===============================
# PROFIT CHART
# ===============================

fig1 = px.bar(
    factory,
    x="Factory",
    y="Average_Profit",
    color="Factory",
    text_auto=True,
    title="Average Profit by Factory"
)

st.plotly_chart(fig1, use_container_width=True)

# ===============================
# SALES CHART
# ===============================

fig2 = px.bar(
    factory,
    x="Factory",
    y="Average_Sales",
    color="Factory",
    text_auto=True,
    title="Average Sales by Factory"
)

st.plotly_chart(fig2, use_container_width=True)

# ===============================
# LEAD TIME
# ===============================

fig3 = px.bar(
    factory,
    x="Factory",
    y="Average_Lead_Time",
    color="Average_Lead_Time",
    text_auto=True,
    title="Average Lead Time by Factory"
)

st.plotly_chart(fig3, use_container_width=True)

# ===============================
# UNITS
# ===============================

fig4 = px.pie(
    factory,
    names="Factory",
    values="Total_Units",
    title="Total Units Manufactured"
)

st.plotly_chart(fig4, use_container_width=True)

# ===============================
# RANKING
# ===============================

st.markdown("---")

st.subheader("🏆 Factory Ranking")

ranking = factory.sort_values(
    by="Average_Profit",
    ascending=False
)

ranking.index = range(1, len(ranking)+1)

st.dataframe(
    ranking,
    use_container_width=True
)