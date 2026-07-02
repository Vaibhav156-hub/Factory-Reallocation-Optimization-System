import streamlit as st
import pandas as pd

df = pd.read_csv("Processed_Nassau_Candy.csv")
st.write(df["Lead_Time"].describe())
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Executive Dashboard", layout="wide")

# Load processed dataset
df = pd.read_csv("Processed_Nassau_Candy.csv")

st.title("📊 Executive Dashboard")
st.markdown("---")

# =======================
# KPI Cards
# =======================

col1, col2, col3, col4 = st.columns(4)

col1.metric("📦 Total Orders", len(df))
col2.metric("🍫 Total Products", df["Product Name"].nunique())
col3.metric("💰 Total Sales", f"${df['Sales'].sum():,.0f}")
col4.metric("📈 Total Profit", f"${df['Gross Profit'].sum():,.0f}")

st.markdown("---")

col5, col6 = st.columns(2)

col5.metric(
    "🚚 Average Lead Time",
    f"{df['Lead_Time'].mean():.2f} Days"
)

col6.metric(
    "📊 Average Sales",
    f"${df['Sales'].mean():.2f}"
)

st.markdown("---")

# =======================
# Sales by Division
# =======================

sales_div = df.groupby("Division", as_index=False)["Sales"].sum()

fig = px.bar(
    sales_div,
    x="Division",
    y="Sales",
    color="Division",
    text_auto=True,
    title="Sales by Division"
)

st.plotly_chart(fig, use_container_width=True)

# =======================
# Profit by Factory
# =======================

profit = df.groupby(
    "Origin_Factory",
    as_index=False
)["Gross Profit"].sum()

fig2 = px.bar(
    profit,
    x="Origin_Factory",
    y="Gross Profit",
    color="Origin_Factory",
    text_auto=True,
    title="Profit by Factory"
)

st.plotly_chart(fig2, use_container_width=True)

# =======================
# Ship Mode
# =======================

fig3 = px.pie(
    df,
    names="Ship Mode",
    title="Shipping Mode Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# =======================
# Top Products
# =======================

top = (
    df.groupby("Product Name", as_index=False)["Sales"]
      .sum()
      .sort_values("Sales", ascending=False)
      .head(10)
)

fig4 = px.bar(
    top,
    x="Sales",
    y="Product Name",
    orientation="h",
    color="Sales",
    text_auto=True,
    title="Top 10 Products by Sales"
)

st.plotly_chart(fig4, use_container_width=True)