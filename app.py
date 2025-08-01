import streamlit as st
import pandas as pd
import order_analytics as oa

st.title("E-commerce Order Analytics")

st.subheader("Users")
total_users_df = pd.DataFrame(oa.total_users, columns=["User ID", "Total Spend"]).set_axis(range(1, len(oa.total_users) + 1))
st.dataframe(total_users_df, height=350, width=700)

st.subheader("Summary Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Orders", oa.total_orders)
col2.metric("Total Revenue", f"₹{oa.total_revenue:,.2f}")
col3.metric("Avg Order Value", f"₹{oa.average_order_value:.2f}")

st.subheader("Revenue Of Last 7 Days")
rev_df = pd.DataFrame({
    "Date": [day.strftime("%Y-%m-%d") for day in oa.last_7_days],
    "Revenue": [oa.revenue_by_day[day] for day in oa.last_7_days]
})
st.bar_chart(rev_df.set_index("Date"))

st.subheader("Order Most Popular Product")
st.write(f"**{oa.most_popular[0]}** - {oa.most_popular[1]} units sold")


st.subheader("Cancellation Rate")
st.write(f"{oa.cancellation_rate:.2f}%")

st.subheader("Top 5 Users by Total Spend")
top_users_df = pd.DataFrame(oa.top_users, columns=["User ID", "Total Spend"]).set_axis(range(1, len(oa.top_users) + 1))
st.table(top_users_df)