import streamlit as st

st.title("AWMA configurator")


door_prices = {
    "834 x 2097": {"Standard": 6328.3, "Full": 7600.41},
    "834 x 2177": {"Standard": 6328.3, "Full": 7600.41},
    "834 x 2397": {"Standard": 6648.74, "Full": 7949.32},
}

door_size = st.selectbox("Select Door Size:", list(door_prices.keys()))
door_type = st.selectbox("Select Door Type:", ["Standard", "Full"])

price = door_prices[door_size][door_type]

st.write(f"Selected Door Size: {door_size}")
st.write(f"Selected Door Type: {door_type}")
st.write(f"Base Price: ${price}")