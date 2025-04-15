import pandas as pd
import numpy as np
from datetime import datetime

# Load the data
df = pd.read_csv("client_portfolio_summary_marvel.csv")
df["net_income"] = df["revenue"] - df["cost"] - df["charge_offs"]

# Convert 'month' column to datetime format
df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

# Sort for consistency
df = df.sort_values(by=["client_name", "month"])

# Prepare result container
forecast_results = []

# Forecast for each client
for client, group in df.groupby("client_name"):
    group = group.set_index("month").resample("M").sum()  # Ensure regular monthly frequency

    # Simple forecast: average monthly growth rate of net_income
    group["net_income_change"] = group["net_income"].diff()
    avg_growth = group["net_income_change"].mean()

    # Get last known net_income and date
    last_date = group.index.max()
    last_value = group.loc[last_date, "net_income"]

    # Forecast next 3 months
    for i in range(1, 4):
        next_month = last_date + pd.DateOffset(months=i)
        next_value = last_value + (avg_growth if not np.isnan(avg_growth) else 0)
        forecast_results.append({
            "client_name": client,
            "forecast_month": next_month.strftime("%Y-%m"),
            "forecast_net_income": round(next_value, 2)
        })
        last_value = next_value

# Convert to DataFrame
forecast_df = pd.DataFrame(forecast_results)

# Show results
print("\nForecasted Net Income (Next 3 Months):")
print(forecast_df.pivot(index="client_name", columns="forecast_month", values="forecast_net_income").fillna(0))
