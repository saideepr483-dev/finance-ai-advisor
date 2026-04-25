import streamlit as st
import pandas as pd

st.set_page_config(page_title="Finance AI Advisor", layout="centered")

# Initialize session data
if "data" not in st.session_state:
    st.session_state.data = pd.DataFrame(
        columns=["Date", "Category", "Amount", "Description"]
    )

st.title("💰 Personal Finance AI Advisor (India)")

# ---- Add Expense ----
st.subheader("Add Expense")

date = st.date_input("Date")
category = st.selectbox(
    "Category",
    ["Food", "Transport", "Shopping", "Bills", "Rent", "UPI", "Other"]
)
amount = st.number_input("Amount (₹)", min_value=0)
description = st.text_input("Description")

if st.button("Add Expense"):
    new_row = {
        "Date": str(date),
        "Category": category,
        "Amount": amount,
        "Description": description
    }
    st.session_state.data.loc[len(st.session_state.data)] = new_row
    st.success("✅ Expense Added!")

# ---- Show Data ----
st.subheader("All Expenses")
st.dataframe(st.session_state.data)

# ---- Analysis ----
if not st.session_state.data.empty:

    st.subheader("📊 Spending Summary")
    summary = st.session_state.data.groupby("Category")["Amount"].sum()
    st.bar_chart(summary)

    # Insights
    st.subheader("🧠 AI Insights")
    total = st.session_state.data["Amount"].sum()
    st.write(f"💰 Total Spending: ₹{total}")

    for cat in summary.index:
        if summary[cat] > 0.4 * total:
            st.warning(f"⚠️ High spending on {cat}")

    # Prediction
    st.subheader("📈 Future Prediction")
    avg = st.session_state.data["Amount"].mean()
    st.write(f"Daily Average: ₹{avg:.2f}")
    st.write(f"Estimated Monthly: ₹{avg*30:.2f}")
