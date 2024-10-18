import pandas as pd
import streamlit as st

from data_processing import getBasePrice

df = pd.read_csv("Door_prices.csv")

st.title("AWMA configurator")
col1, col2 = st.columns(2)

door_prices = getBasePrice(df)
with col1:
    door_size = st.selectbox("Select Door Size:", list(door_prices.keys()))
    st.write(f"Selected Door Size: {door_size}")
with col2:
    door_type = st.selectbox("Select Door Type:", ["Standard", "Fully Sealed"])
    st.write(f"Selected Door Type: {door_type}")

price = door_prices[door_size][door_type]
st.write("Base Price:" + price)