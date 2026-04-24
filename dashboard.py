import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# ---------------- DB CONNECTION ----------------
username = "root"
password = "password%40123"
host = "localhost"
port = "3306"
database = "customer_behavior"

engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

st.set_page_config(page_title="Customer Dashboard", layout="wide")

st.title("📊 Customer Behavior Analytics Dashboard")

# ---------------- LOAD DATA ----------------
df = pd.read_sql("SELECT * FROM customer", engine)

# ---------------- SIDEBAR FILTERS ----------------
st.sidebar.header("🔍 Filters")

gender_filter = st.sidebar.multiselect("Select Gender", df['gender'].unique(), default=df['gender'].unique())
age_filter = st.sidebar.multiselect("Select Age Group", df['age_group'].unique(), default=df['age_group'].unique())
subscription_filter = st.sidebar.multiselect("Subscription", df['subscription_status'].unique(), default=df['subscription_status'].unique())

filtered_df = df[
    (df['gender'].isin(gender_filter)) &
    (df['age_group'].isin(age_filter)) &
    (df['subscription_status'].isin(subscription_filter))
]

# ---------------- KPIs ----------------
total_revenue = filtered_df['purchase_amount'].sum()
total_customers = filtered_df['customer_id'].count()
avg_purchase = filtered_df['purchase_amount'].mean()
repeat_buyers = filtered_df[filtered_df['previous_purchases'] > 5]['customer_id'].count()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("👥 Customers", total_customers)
col3.metric("📦 Avg Purchase", f"₹{avg_purchase:,.2f}")
col4.metric("🔁 Repeat Buyers", repeat_buyers)

st.markdown("---")

# ---------------- CHARTS ----------------

# Revenue by Gender
st.subheader("👨‍👩‍👧 Revenue by Gender")
gender_df = filtered_df.groupby('gender')['purchase_amount'].sum()
st.bar_chart(gender_df)

# Top 5 Products
st.subheader("🛍️ Top 5 Products by Rating")
top_products = filtered_df.groupby('item_purchased')['review_rating'].mean().sort_values(ascending=False).head(5)
st.bar_chart(top_products)

# Shipping Type
st.subheader("🚚 Shipping Type Analysis")
shipping_df = filtered_df.groupby('shipping_type')['purchase_amount'].mean()
st.bar_chart(shipping_df)

# Subscription Analysis
st.subheader("💳 Subscription Analysis")
subscription_df = filtered_df.groupby('subscription_status').agg({
    'customer_id': 'count',
    'purchase_amount': ['mean', 'sum']
})
st.dataframe(subscription_df)

# Discount Usage
st.subheader("🏷️ Discount Usage (%)")
discount_df = filtered_df.groupby('item_purchased').apply(
    lambda x: (x['discount_applied'] == 'Yes').sum() / len(x) * 100
).sort_values(ascending=False).head(5)

st.bar_chart(discount_df)

# Customer Segmentation
st.subheader("👥 Customer Segmentation")

def segment(x):
    if x == 1:
        return "New"
    elif 2 <= x <= 10:
        return "Returning"
    else:
        return "Loyal"

filtered_df['segment'] = filtered_df['previous_purchases'].apply(segment)

segment_df = filtered_df['segment'].value_counts()
st.bar_chart(segment_df)

# Age Group Revenue
st.subheader("🎂 Revenue by Age Group")
age_df = filtered_df.groupby('age_group')['purchase_amount'].sum()
st.bar_chart(age_df)

st.markdown("---")

st.success("✅ Dashboard Ready!")