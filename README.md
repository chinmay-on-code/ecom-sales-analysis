// ...existing code...
# ecom-sales-analysis

Exploratory analysis of Olist e‑commerce sales data using Python. Analyzes trends over time, top product categories, seller performance, and geographic distribution. Includes data cleaning, visualizations, and stakeholder-ready insights.

---

## One-line summary
Structured EDA that translates raw marketplace data into business insights: monthly trends, top categories, seller performance, and geographic opportunities to inform growth and operations.

---

## 1) Problem (Business Pain)
Marketplaces need to know where revenue is concentrated, which products and sellers drive growth, and which regions underperform. Without these insights, marketing and operations cannot target improvements in revenue, fulfillment, or seller incentives.

---

## 2) My Role
- Led the end‑to‑end exploratory analysis.
- Designed the data pipeline, performed cleaning and joins, created visualizations, and summarized key insights for stakeholders.
- Collaborated with product/ops (hypothetical) to translate findings into action recommendations.

---

## 3) Data — source, type & scale
- Source: Olist public e‑commerce dataset (multiple CSV tables).
- Key tables used: orders, order_items, products, customers, sellers, product_category_name_translation.
- Type: transactional tables with timestamps, categorical labels, numeric price fields.
- Scale: tens to hundreds of thousands of rows across tables (order-level + item-level records).

---

## 4) Tools & Techniques (why each was used)
- Python + pandas — data cleaning, merges, aggregations.
- Jupyter Notebook — interactive EDA and narrative.
- Matplotlib — time series and categorical visualizations for stakeholder communication.
- Aggregation & grouping — compute KPIs (revenue, orders, AOV).
- Time-series bucketing (monthly) — trend detection.
- Geographic grouping — state-level revenue and seller distribution.

---

## 5) Process / Pipeline
1. Load CSVs into pandas DataFrames.
2. Convert timestamps and filter delivered orders.
3. Merge order / item / product / customer / seller tables.
4. Create derived fields (order_month, product_category_name_english).
5. Aggregate by month, category, seller, and state.
6. Visualize results and extract business-focused insights.
7. Summarize KPIs and recommendations.

---

## 6) Key Insights (examples)
- Clear seasonality in monthly revenue and order volume; peak months identified.
- Top product categories drive a large share of orders — prioritize inventory and promotions there.
- A small set of sellers generates the most revenue — consider partnership programs.
- Revenue concentrated in a few states — targeted logistics/marketing can improve ROI.

---

## 7) Business Impact (how to convert insights to value)
- Focus marketing spend on top categories + peak months to increase ROI.
- Incentivize high-performing sellers to increase retention and average order value.
- Optimize fulfillment/network in top revenue states to reduce delivery time and costs.
- Expected outcomes: higher conversion on promotions, lower fulfillment costs, and improved seller retention.

---

## 8) Challenges & Learnings
- Handling missing category translations and inconsistent timestamps required robust cleaning.
- Many-to-one joins increased record counts — careful deduplication and join logic were necessary.
- Learned to frame EDA results as business actions (not just charts): actionable recommendations are what stakeholders value.

---

## How to run
1. Create virtual env and install deps:
   - python -m venv .venv
   - source .venv/bin/activate
   - pip install -r requirements.txt
2. Open the notebook:
   - jupyter notebook EDA.ipynb
3. Run cells to reproduce charts and KPIs.

---

## Notes for interviews / portfolio
Use the cheat‑sheet approach:
- Start with the business pain → state the measurable outcome you targeted.
- Explain your specific role and decisions.
- Describe the data (source, type, scale).
- Tie tools to outcomes (e.g., "pandas to join tables and compute monthly KPIs").
- Finish with one key insight, the recommended business action, and a measurable impact.

---
