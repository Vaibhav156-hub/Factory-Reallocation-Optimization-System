import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="What-If Analysis",
    layout="wide"
)

# ===========================================
# LOAD DATA
# ===========================================

recommendation = pd.read_csv("Factory_Optimization_Recommendations.csv")

st.title("🔄 What-If Scenario Analysis")

st.markdown("""
Compare the current factory assignment with the recommended factory assignment.
""")

st.markdown("---")

# ===========================================
# PRODUCT SELECTOR
# ===========================================

product = st.selectbox(
    "Select Product",
    sorted(recommendation["Product"].unique())
)

row = recommendation[
    recommendation["Product"] == product
].iloc[0]

# ===========================================
# METRICS
# ===========================================

col1, col2 = st.columns(2)

col1.metric(
    "Current Factory",
    row["Current Factory"]
)

col2.metric(
    "Recommended Factory",
    row["Recommended Factory"]
)

st.markdown("---")

col3, col4, col5 = st.columns(3)

col3.metric(
    "Current Lead Time",
    f"{row['Current Lead Time']:.2f} Days"
)

col4.metric(
    "Predicted Lead Time",
    f"{row['Predicted Lead Time']:.2f} Days"
)

col5.metric(
    "Improvement",
    f"{row['Lead Time Improvement']:.2f} Days"
)

# ===========================================
# BAR CHART
# ===========================================

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

    title="Lead Time Comparison"

)

st.plotly_chart(fig, use_container_width=True)

# ===========================================
# IMPROVEMENT MESSAGE
# ===========================================

if row["Lead Time Improvement"] > 0:

    st.success(
        f"✅ Switching to {row['Recommended Factory']} reduces lead time by {row['Lead Time Improvement']:.2f} days."
    )

else:

    st.info(
        "No improvement expected."
    )

# ===========================================
# DETAILS TABLE
# ===========================================

st.markdown("---")

st.subheader("Scenario Details")

st.dataframe(
    row.to_frame().T,
    use_container_width=True
)