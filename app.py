import streamlit as st

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Factory Optimization System",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# MAIN TITLE
# --------------------------------------------------
st.title("🏭 Factory Reallocation & Shipping Optimization Recommendation System")

st.markdown("---")

st.markdown("""
### Welcome

This dashboard helps analyze and optimize factory allocation for **Nassau Candy Distributor**.

### Features

- 📊 Executive Dashboard
- 🏭 Factory Performance Analysis
- 🤖 Recommendation Engine
- 🔄 What-If Scenario Analysis
- 📈 Route Clustering
- 📥 Download Recommendations

---

### Project Objective

Predict shipping performance and recommend better factory assignments to reduce lead time while maintaining profitability.

Use the **left sidebar** to navigate between dashboard pages.
""")

st.success("Project Successfully Loaded ✅")

st.sidebar.title("🏭 Navigation")
st.sidebar.info(
    """
Use the pages in the sidebar to explore:

• Executive Dashboard

• Factory Performance

• Recommendation Engine

• What-If Analysis

• Route Clustering
"""
)

st.markdown("---")

st.caption(
    "Developed using Python, Streamlit, Scikit-Learn, Pandas, Plotly and Machine Learning."
)