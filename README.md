# Supermarket Sales Dashboard

This Sales Dashboard is a data analysis and visualization project created in Python using Streamlit, pandas, and Plotly Express. It allows users to interactively explore and gain insights from a sales dataset. The dashboard provides key performance indicators (KPIs), product line sales, and hourly sales breakdown, enabling users to make data-driven decisions based on the available data.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Dataset](#dataset)
- [Features](#features)
- [How to Use the Dashboard](#how-to-use-the-dashboard)
- [Key Performance Indicators (KPIs)](#key-performance-indicators-kpis)
- [Sales by Product Line](#sales-by-product-line)
- [Sales by Hour](#sales-by-hour)
- [Code](#code)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This Sales Dashboard project is designed to provide valuable insights into a sales dataset. It can be used by sales professionals, data analysts, and decision-makers to analyze sales trends and make informed decisions based on the data.

## Getting Started

To run this Sales Dashboard on your local machine, follow these steps:

1. Clone this repository.
2. Ensure you have Python installed.
3. Install the required libraries by running: `pip install -r requirements.txt`.
4. Execute the dashboard using Streamlit: `streamlit run sales_dashboard.py`.

## Dataset

The dataset used in this dashboard is named "supermarkt_sales.xlsx" and is an Excel file. It contains sales data from a supermarket, including information about the city, customer type, gender, product line, sales totals, ratings, and timestamps.

## Features

- Interactive data filtering by city, customer type, and gender.
- Key performance indicators (KPIs) for quick insights.
- Visualization of sales by product line in a bar chart.
- Visualization of sales by hour in another bar chart.

## How to Use the Dashboard

1. Select the desired filters in the sidebar to narrow down the dataset.
2. Observe the key performance indicators (KPIs) at the top of the dashboard, providing an overview of the filtered data.
3. Explore the sales by product line and sales by hour visualizations to understand sales trends.

## Key Performance Indicators (KPIs)

The KPIs provide a quick snapshot of the filtered data:

- **Total Sales**: The total sales amount in US dollars.
- **Average Rating**: The average rating with a star rating representation.
- **Average Sales Per Transaction**: The average sales per transaction in US dollars.

## Sales by Product Line

The bar chart visualizes sales by product line, helping to identify the most and least popular product categories.

## Sales by Hour

The bar chart shows how sales vary by hour of the day, helping to understand sales patterns throughout the day.

## Code

The code for this Sales Dashboard is implemented in Python using Streamlit, pandas, and Plotly Express. You can find the main application code in the [app.py](app.py) file.

