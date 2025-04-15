# Bread Money

Bread Money is a simulated financial analytics dashboard modeled. It combines real-world data analysis, forecasting, and interactive visualizations to demonstrate credit card client profitability and strategy.

---

## Project Overview

**Purpose**: Analyze and forecast client profitability across branded credit card portfolios.

**Tools Used**:
- Python (pandas, plotly)
- Streamlit (frontend dashboard)
- ExcelWriter (automated reporting)
- Jupyter + CLI-based script workflows

**Key Features**:
- Net income analysis (revenue - cost - charge-offs)
- Forecasted net income for the next 3 months
- Interactive dashboard with filters and charts
- Auto-generated Excel report with styling

---

## Folder Structure

``` text
SHIELD-MONEY/
├── analytics/
│   ├── client_analysis.py
│   ├── forecast.py
│   └── export_report.py
├── dashboard/
│   └── bread_money_dashboard.py
├── client_portfolio_summary_marvel.csv
├── client_net_income_report.xlsx
└── README.md
```

---

## Usage

1. Clone the repo:
```bash
git clone https://github.com/yourusername/bread-money.git
cd bread-money
```

2. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the analysis:
```bash
python3 analytics/client_analysis.py
python3 analytics/forecast.py
python3 analytics/export_report.py
```

5. Start the dashboard:
```bash
streamlit run dashboard/bread_money_dashboard.py
```

---

## Demo Data

The included dataset simulates:
- 12 months of performance for 10 Marvel-themed credit card brands
- Monthly data points: active accounts, average spend, revenue, cost, charge-offs

---

## Author

**Amos K. Agyeman**  

---

## License

MIT License. Free to use, build upon, and showcase.

