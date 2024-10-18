import pandas as pd
import streamlit as st

from data_processing import getBasePrice

df = pd.read_csv("Door_prices.csv")

st.title("AWMA configurator")

door_prices = getBasePrice(df)

door_size = st.selectbox("Select Door Size:", list(door_prices.keys()))
door_type = st.selectbox("Select Door Type:", ["Standard", "Fully Sealed"])

price = door_prices[door_size][door_type]

st.write(f"Selected Door Size: {door_size}")
st.write(f"Selected Door Type: {door_type}")
st.write(f"Base Price: ${price}")