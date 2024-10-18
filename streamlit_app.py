import pandas as pd
import streamlit as st

from data_processing import getBasePrice

df = pd.read_csv("Door_prices.csv")

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
    if door_type == "Standard":
        mortice = st.selectbox("Mortice:", ["Universal Mortice Lock 3772TSC", 
                                            "Australian Oval Cylinder"])
        latchPlate = st.selectbox("Latch Plate:",["Standard Erntec Latch",
                                                  "Striker, Electric, 12-30Vdc, 25kg Pre-Load, Multi-function, No-Lip"])


    elif door_type == "Fully Sealed":
        mortice = st.selectbox("Mortice:", ["Universal Mortice Lock 3772TSC", "Australian Oval Cylinder"])
        latchPlate = st.selectbox("Latch Plate:",["Standard Erntec Latch FS",
                                                  "Striker, Electric, 12-30Vdc, 25kg Pre-Load, Multi-function, No-Lip"])

holder = ["Custom Latch Block:", "Exterior Plate/ Handle:", "Interior Plate/ Handle:", "Additional Hardware:"]

