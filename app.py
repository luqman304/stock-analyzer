import streamlit as st
from analyzer import get_stock_data, plot_stock_data

st.title("📈 Stock Analyzer")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA):")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Analyze") and ticker:
    df = get_stock_data(ticker, start_date, end_date)
    if df is not None:
        st.write(f"Showing data for: **{ticker.upper()}**")
        st.dataframe(df.tail())
        plot_stock_data(df, ticker)
    else:
        st.error("Could not fetch data. Check the ticker symbol.")