import pandas as pd
import numpy as np

# Load actual data
df = pd.read_csv("client_portfolio_summary_marvel.csv")
df["net_income"] = df["revenue"] - df["cost"] - df["charge_offs"]
df["month"] = pd.to_datetime(df["month"], format="%Y-%m")

# Create Net Income History sheet
net_income_history = df.pivot_table(
    index="client_name",
    columns=df["month"].dt.strftime("%Y-%m"),
    values="net_income",
    aggfunc="sum"
).fillna(0).round(2)

net_income_history["Total_Net_Income"] = net_income_history.sum(axis=1)

# Forecast (same logic as before)
forecast_results = []
for client, group in df.groupby("client_name"):
    group = group.set_index("month").resample("M").sum()
    group["net_income_change"] = group["net_income"].diff()
    avg_growth = group["net_income_change"].mean()

    last_date = group.index.max()
    last_value = group.loc[last_date, "net_income"]

    for i in range(1, 4):
        next_month = last_date + pd.DateOffset(months=i)
        next_value = last_value + (avg_growth if not np.isnan(avg_growth) else 0)
        forecast_results.append({
            "client_name": client,
            "forecast_month": next_month.strftime("%Y-%m"),
            "forecast_net_income": round(next_value, 2)
        })
        last_value = next_value

# Convert forecast to pivot table
forecast_df = pd.DataFrame(forecast_results)
forecast_pivot = forecast_df.pivot(
    index="client_name",
    columns="forecast_month",
    values="forecast_net_income"
).fillna(0).round(2)

# Export to Excel
output_path = "analytics/client_net_income_report.xlsx"
with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
    net_income_history.to_excel(writer, sheet_name="Net_Income_History")
    forecast_pivot.to_excel(writer, sheet_name="Forecast_Net_Income")

print(f"\n Excel report saved to: {output_path}")
