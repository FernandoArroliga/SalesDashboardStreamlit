# Importing the useful libraries and modules
import pandas as pd
import plotly.express as px
import streamlit as st

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/

# Setting the Streamlit App
st.set_page_config(page_title="Sales Dashboard",
                   page_icon=":bar_chart:",
                   layout="wide")

# Loading the data
data = pd.read_excel(
    io="supermarkt_sales.xlsx",
    engine="openpyxl",
    sheet_name="Sales",
    skiprows=3,
    usecols="B:R",
    nrows=1000,)

# --------- SIDEBAR ----------
st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select the City:",
    options=data["City"].unique(),
    default=data["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options=data["Customer_type"].unique(),
    default=data["Customer_type"].unique()
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options=data["Gender"].unique(),
    default=data["Gender"].unique()
)

data_selection = data.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

#st.dataframe(data_selection)

# --------- MAINPAGE --------------
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

# TOP KPI´S
total_sales = int(data_selection["Total"].sum())
average_rating = round(data_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(data_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)

with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")

with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"US $ {average_rating} {star_rating}")

with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("---")











