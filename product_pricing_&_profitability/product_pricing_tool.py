# Import python packages
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Initialize Snowflake session.
from snowflake.snowpark.context import get_active_session
session = get_active_session()

# Load the product_details view data into a Pandas data frame.
df_products = session.table("product_details").to_pandas()

# Title
st.title('Product Pricing Tool')
# subheader
st.write('This app displays the pricing, profit margin, and revenue for each product.')

# creating a sidebar for the app
st.sidebar.subheader("Data Filtering Options", divider="gray")
    
# creating 3 multiselects or drop-downs that allow users to filter visuals by:
# product department (e.g. men, women), product category (e.g. accessories, active), and product brand (e.g. Nike, Under Armour)
    
# department filter
department_list = sorted(df_products['DEPARTMENT'].unique().tolist())
department_selection = st.sidebar.multiselect('Department', department_list)

# product category filter
category_list = sorted(df_products['CATEGORY'].unique().tolist())
category_selection = st.sidebar.multiselect('Category', category_list)

# product brand filter
brand_list = sorted([brand for brand in df_products['BRAND'].dropna().unique().tolist()])
brand_selection = st.sidebar.multiselect('Brand', brand_list)

# Next, apply filters to data.

# create a copy of the dataframe
# if no filters are applied then the app will just go with the original, copied dataframe or filtered_data
filtered_data = df_products.copy()

# if a specific category(s) is chosen, the app will filter the products based on the category(s) chosen
if department_selection:
    filtered_data = filtered_data[filtered_data['DEPARTMENT'].isin(department_selection)]
if category_selection:
    filtered_data = filtered_data[filtered_data['CATEGORY'].isin(category_selection)]
if brand_selection:
    filtered_data = filtered_data[filtered_data['BRAND'].isin(brand_selection)]

# In the body of the app, include 4 metrics in a horizontal column:
    # 1. Products (Count)
    # 2. Total Sales ($K)
    # 3. Average Product Sales ($K)
    # 4. Average Profit Margin (%)
# The metrics should change when filters are applied.
# Do NOT use any "delta" indicators.

# calculate metrics from filtered data
product_count = filtered_data['PRODUCT_ID'].nunique()
total_sales_k = round(filtered_data['TOTAL_SALES'].sum() / 1000, 2) # divide by 1000 to convert to thousands and round to 2 decimal places
avg_sales_k = round(filtered_data['TOTAL_SALES'].mean() / 1000, 2) # average total sales per product (also in $K)
avg_margin_pct = round(filtered_data['MARGIN_PCT'].mean() * 100, 2) # average profit margin (in %)

# create a row of metrics
col1, col2, col3, col4 = st.columns(4)

# Apply commas using f-strings for products sold and total sales
col1.metric("Total Number of Products Sold", f"{product_count:,}") # ':,' adds commas as thousands separators
col2.metric("Total Sales ($K)", f"{total_sales_k:,.2f}") # '.2f' ensures two decimal places (for sales)
col3.metric("Average Product Sales ($K)", avg_sales_k)
col4.metric("Average Profit Margin (%)", f"{avg_margin_pct}%")

# Also, in the body of the app, include three charts:
    # 1. A distribution of product prices
    # 2. A distribution of product profit margins (%)
    # 3. The count of products in each category
      # - above each chart, include a subheader and overview
      # - in the 3rd chart, the categories should be alphabetized

# Chart 1 - a histogram showing the distributiion of product prices.
st.subheader('Distribution of Product Prices')
st.write('The chart shows how product prices are distributed across the dataset.')
pp = sns.displot(data=filtered_data, x="RETAIL_PRICE", bins=20, kde=True)

# Axis labels
pp.set_axis_labels("Retail Price ($)", "Number of Products")


st.pyplot(pp.fig)

# Chart 2 - a histogram showing the distribution of product profit margins
st.subheader('Distribution of Product Profit Margins (%)')
st.write ('The chart displays how profit margins percentages are distrubted across the dataset.')

# a temporary column with whole number percentages (in the dataset, the margin_pct is in decimal form)
filtered_data['MARGIN_PCT_WHOLE'] = filtered_data['MARGIN_PCT'] * 100

pp_pct = sns.displot(data=filtered_data, x="MARGIN_PCT_WHOLE", bins=20)

# Axis labels
pp_pct.set_axis_labels("Profit Magin (%)", "Number of Products")

st.pyplot(pp_pct.fig)

# Chart 3 - the count of products in each category
st.subheader('Products by Category')
st.write ('This chart shows the distribution of products across categories.')

# Create figure and axes (width and height)
fig, ax = plt.subplots(figsize=(10, 8)) # figsize=(width, height)


sns.countplot(data=filtered_data, y="CATEGORY", ax=ax) 

# Axis labels
ax.set_ylabel("Category")
ax.set_xlabel("Number of Products")

st.pyplot(fig)
