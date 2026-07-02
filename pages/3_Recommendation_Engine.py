import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Recommendation Engine",
    layout="wide"
)

# ======================================
# LOAD DATA
# ======================================

recommendation = pd.read_csv("Factory_Optimization_Recommendations.csv")

st.title("🤖 Factory Recommendation Engine")

st.markdown(
"""
Select a product to view the recommended factory and expected operational improvement.
"""
)

st.markdown("---")

# ======================================
# PRODUCT SELECTOR
# ======================================

product = st.selectbox(
    "📦 Select Product",
    sorted(recommendation["Product"].unique())
)

row = recommendation[
    recommendation["Product"] == product
].iloc[0]

# ======================================
# KPI CARDS
# ======================================

col1, col2 = st.columns(2)

col1.metric(
    "🏭 Current Factory",
    row["Current Factory"]
)

col2.metric(
    "✅ Recommended Factory",
    row["Recommended Factory"]
)

st.markdown("")

col3, col4, col5 = st.columns(3)

col3.metric(
    "🚚 Current Lead Time",
    f"{row['Current Lead Time']:.2f} Days"
)

col4.metric(
    "⚡ Predicted Lead Time",
    f"{row['Predicted Lead Time']:.2f} Days"
)

col5.metric(
    "📉 Improvement",
    f"{row['Lead Time Improvement']:.2f} Days"
)

st.markdown("---")

# ======================================
# RECOMMENDATION TABLE
# ======================================

st.subheader("📋 Recommendation Details")

st.dataframe(
    row.to_frame().T,
    use_container_width=True
)

# ======================================
# BAR CHART
# ======================================

compare = pd.DataFrame({
    "Scenario":[
        "Current",
        "Recommended"
    ],
    "Lead Time":[
        row["Current Lead Time"],
        row["Predicted Lead Time"]
    ]
})

fig = px.bar(
    compare,
    x="Scenario",
    y="Lead Time",
    color="Scenario",
    text_auto=True,
    title="Current vs Recommended Lead Time"
)

st.plotly_chart(fig, use_container_width=True)

# ======================================
# DOWNLOAD BUTTON
# ======================================

st.download_button(
    "📥 Download Recommendations",
    recommendation.to_csv(index=False),
    file_name="Factory_Recommendations.csv",
    mime="text/csv"
)

# ======================================
# COMPLETE TABLE
# ======================================

st.markdown("---")

st.subheader("📊 All Product Recommendations")

st.dataframe(
    recommendation,
    use_container_width=True
)