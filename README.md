# E-Commerce Shipping & Delivery Analysis

An interactive data analytics dashboard built using Python and Streamlit to analyze e-commerce delivery performance, shipping trends, seller performance, and logistics operations.

## Project Overview

The E-Commerce Shipping Intelligence Dashboard transforms e-commerce shipping data into meaningful insights through interactive KPIs, charts, geographical visualizations, and business recommendations.

## Features

- **Executive Overview:** Key performance indicators and delivery summaries.
- **Delivery Analytics:** Delivery trends, delays, and performance analysis.
- **Geographical Insights:** Interactive Brazil delivery map and state-level analysis.
- **Seller Performance:** Seller rankings and performance comparisons.
- **Logistics Intelligence:** Carrier and handoff performance analysis.
- **Business Insights:** Data-driven findings and recommendations.

## Technologies Used

- Python
- Pandas
- Streamlit
- Plotly
- HTML and CSS
- VS Code

## Project Structure

```text
Ecommerce_Shipping_Analysis/
│
├── data/
│   ├── processed/
│   │   ├── carrier_handoff_results.csv
│   │   ├── delivered_orders.csv
│   │   ├── delivery_kpi_results.csv
│   │   ├── monthly_handoff_report.csv
│   │   ├── orders_processed.csv
│   │   ├── seller_performance_report.csv
│   │   └── state_delivery_report.csv
│   │
│   └── raw/
│       ├── olist_customers_dataset.csv
│       ├── olist_geolocation_dataset.csv
│       ├── olist_order_items_dataset.csv
│       ├── olist_order_payments_dataset.csv
│       ├── olist_order_reviews_dataset.csv
│       ├── olist_orders_dataset.csv
│       ├── olist_products_dataset.csv
│       ├── olist_sellers_dataset.csv
│       └── product_category_name_translation.csv
│
├── outputs/
│   └── charts/
│       ├── bottom_sellers.png
│       ├── brazil_delivery_map.html
│       ├── delivery_stage_comparison.png
│       ├── delivery_status.png
│       ├── monthly_delivery.png
│       ├── monthly_handoff_performance.png
│       ├── state_delivery_performance.png
│       ├── top_sellers.png
│       └── weekday_weekend.png
│
├── src/
│   ├── carrier_handoff_analysis.py
│   ├── check_dataset.py
│   ├── delivery_kpi_analysis.py
│   ├── explore_dataset.py
│   ├── preprocess_data.py
│   ├── seller_performance_analysis.py
│   ├── state_delivery_analysis.py
│   ├── state_delivery_map.py
│   ├── visualize_delivery.py
│   ├── visualize_handoff.py
│   └── visualize_seller_performance.py
│
├── app.py
├── README.md
└── requirements.txt

```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd Ecommerce_Shipping_Analysis
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the dashboard

```bash
python -m streamlit run app.py
```

The dashboard will open in your browser.

## Dashboard Pages

1. Executive Overview
2. Delivery Analytics
3. Geographical Insights
4. Seller Performance
5. Logistics Intelligence
6. Business Insights

## Project Objective

The objective is to identify delivery delays, evaluate seller performance, analyze logistics efficiency, understand geographical delivery patterns, and support data-driven business decisions.

## Author

**Vidyalakshmee Beerappa Habagonde**

BE Computer Science and Engineering

## Project Status

Dashboard development and initial functional testing completed.