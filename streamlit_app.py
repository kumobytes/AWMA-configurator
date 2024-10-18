import pandas as pd
import streamlit as st

from data_processing import getBasePrice, getHWPrice

df = pd.read_csv("Door_prices.csv")
df1 = pd.read_csv("Hardware_prices.csv", encoding="latin-1")

st.title("AWMA configurator")

st.write("Step 1: Select type of door and size")
col1, col2 = st.columns(2)

door_prices = getBasePrice(df)
with col1:
    door_type = st.radio("Select Door Type:", ["Standard", "Fully Sealed"], horizontal = True)
    st.write(f"Selected Door Type: {door_type}")
with col2:
    door_size = st.selectbox("Select Door Size:", list(door_prices.keys()))
    st.write(f"Selected Door Size: {door_size}")

price = door_prices[door_size][door_type]
#st.write("Base Price:" + price)

st.divider()

st.write("Step 2: Select hinge side")
hinge_type = st.radio("Select Hinge Type:", ["Left hinge", "Right hinge"], horizontal = True)

st.divider()

st.write("Step 3: Select hardware required")


### need review!! door type can be examined here but we need to adopt csv as input
if door_type in door_prices[door_size]:
    # Add conditional hardware options based on door type
    HW_prices = getHWPrice(df1, door_type)

    total_price = 0

    for category, items in HW_prices.items():
        # Create a selection box for each category
        selected_item = st.selectbox(f"Select {category}:", list(items.keys()))
    
        # Display the price of the selected item
        price_str = items[selected_item].strip().replace('$', '').replace(',', '')
        price = float(price_str)
        total_price += price
        #st.write(f"Price for {selected_item}: {price}")

st.divider()

st.write(f"### Total Price: ${total_price:.2f}")

holder = ["Mortice:","Latch Plate:","Custom Latch Block:", "Exterior Plate/ Handle:", "Interior Plate/ Handle:", "Additional Hardware:"]

