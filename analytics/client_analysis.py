import pandas as pd

# Load the Marvel-themed portfolio dataset
df = pd.read_csv("client_portfolio_summary_marvel.csv")

# Step 1: Compute Net Income = Revenue - Cost - Charge Offs
df["net_income"] = df["revenue"] - df["cost"] - df["charge_offs"]

# Step 2: Group by client and month
monthly_summary = df.groupby(["client_name", "month"]).agg({
    "active_accounts": "sum",
    "revenue": "sum",
    "cost": "sum",
    "charge_offs": "sum",
    "net_income": "sum"
}).reset_index()

# Step 3: Show top 5 most profitable clients (total net income)
profit_by_client = monthly_summary.groupby("client_name")["net_income"].sum().sort_values(ascending=False)

print("\nTop 5 Most Profitable Clients (All Time):")
print(profit_by_client.head())

# Step 4: Preview last 3 months of net income by client
latest_months = monthly_summary["month"].sort_values(ascending=False).unique()[:3]
recent = monthly_summary[monthly_summary["month"].isin(latest_months)]

print("\nNet Income for Last 3 Months:")
print(recent.pivot(index="client_name", columns="month", values="net_income").fillna(0).round(2))
