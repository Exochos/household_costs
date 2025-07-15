import streamlit as st
import pandas as pd

st.set_page_config(page_title="Monthly Burn Rate", page_icon="💸", layout="centered")

st.title("💸 Household Monthly Burn Rate")

# Expense categories
categories = [
    "Rent / Mortgage",
    "Utilities",
    "Internet",
    "Phone",
    "Groceries",
    "Dining Out",
    "Insurance",
    "Transportation",
    "Subscriptions",
    "Repairs / Maintenance",
    "Miscellaneous"
]

# Sidebar inputs
st.sidebar.header("Monthly Expenses")
expenses = {}
for category in categories:
    expenses[category] = st.sidebar.number_input(f"{category}", min_value=0.0, step=10.0)

# DataFrame and calculations
df = pd.DataFrame(expenses.items(), columns=["Category", "Amount"])
total = df["Amount"].sum()

# Display
st.subheader("💰 Breakdown")
st.dataframe(df.set_index("Category"))

st.metric("🔥 Total Burn Rate", f"${total:,.2f}")

# Optional: Charts
st.subheader("📊 Visualization")
st.bar_chart(df.set_index("Category"))
if st.checkbox("Show pie chart"):
    st.pyplot(df.set_index("Category").plot.pie(y="Amount", autopct='%1.1f%%', figsize=(5, 5)).figure)
