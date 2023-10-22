# Supermarket Sales Dashboard

This Sales Dashboard is a data analysis and visualization project created in Python using Streamlit, pandas, and Plotly Express. It allows users to interactively explore and gain insights from a sales dataset. The dashboard provides key performance indicators (KPIs), product line sales, and hourly sales breakdown, enabling users to make data-driven decisions based on the available data.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
- [Dataset](#dataset)
- [Features](#features)
- [How to Use the Dashboard](#how-to-use-the-dashboard)
- [Key Performance Indicators (KPIs)](#key-performance-indicators-kpis)
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

You can find the dataset in: [supermarkt_sales.xlsx](supermarkt_sales.xlsx) 

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


## Code

The code for this Sales Dashboard is implemented in Python using Streamlit, pandas, and Plotly Express. You can find the main application code in the [app.py](app.py) file.


## Contributing

We welcome contributions to this project. If you have suggestions for improvements, bug reports, or would like to contribute code, please follow the guidelines below:

1. Fork the repository on GitHub.
2. Clone the forked repository to your local machine.
3. Create a new branch to work on your feature or bug fix.
4. Make your changes and ensure they are properly tested.
5. Commit your changes with clear and concise commit messages.
6. Push your changes to your fork on GitHub.
7. Create a pull request from your fork to the original repository.
8. Provide a detailed description of your changes and any relevant information.

We'll review your pull request and, if it aligns with the project's goals and standards, merge it. Thank you for contributing to our project!

### Reporting Issues

If you find any issues with the project or have suggestions for improvements, please feel free to open a GitHub issue. We appreciate your feedback and will address issues as soon as possible.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
