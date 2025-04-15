import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config
st.set_page_config(page_title="Bread Money Dashboard", layout="wide")
st.title("💳 Bread Money - Client Profitability Dashboard")

# Load data
@st.cache_data

def load_data():
    return pd.read_csv("client_portfolio_summary_marvel.csv")

df = load_data()

df["net_income"] = df["revenue"] - df["cost"] - df["charge_offs"]
df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

# Sidebar filters
clients = sorted(df["client_name"].unique())
selected_clients = st.sidebar.multiselect("Select Clients", clients, default=clients)

filtered_df = df[df["client_name"].isin(selected_clients)]

# Key metrics
total_revenue = filtered_df["revenue"].sum()
total_cost = filtered_df["cost"].sum()
total_net_income = filtered_df["net_income"].sum()
total_charge_offs = filtered_df["charge_offs"].sum()

st.markdown("### Portfolio Summary")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Cost", f"${total_cost:,.0f}")
col3.metric("Net Income", f"${total_net_income:,.0f}")
col4.metric("Charge-Offs", f"${total_charge_offs:,.0f}")

# Line chart of Net Income by Month
monthly_income = (
    filtered_df.groupby(["month", "client_name"])["net_income"].sum().reset_index()
)
fig = px.line(
    monthly_income,
    x="month",
    y="net_income",
    color="client_name",
    title="Net Income Over Time"
)
fig.update_layout(margin=dict(l=20, r=20, t=40, b=20))
st.plotly_chart(fig, use_container_width=True)

# Bar chart of Revenue vs. Cost
st.markdown("### Revenue vs. Cost by Client")
agg_df = filtered_df.groupby("client_name")[["revenue", "cost"]].sum().reset_index()
fig2 = px.bar(
    agg_df.melt(id_vars="client_name", value_vars=["revenue", "cost"]),
    x="client_name",
    y="value",
    color="variable",
    barmode="group",
    title="Revenue and Cost by Client"
)
fig2.update_layout(xaxis_title="Client", yaxis_title="Amount ($)", margin=dict(l=20, r=20, t=40, b=20))
st.plotly_chart(fig2, use_container_width=True)

# Show raw data
with st.expander("🔍 View Raw Data"):
    st.dataframe(filtered_df.sort_values(by="month", ascending=False))
