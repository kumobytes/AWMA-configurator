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
with col2:
    door_size = st.selectbox("Select Door Size:", list(door_prices.keys()))

doorprice = door_prices[door_size][door_type]

# st.write(f"Selected Door Type: {door_type}")
# st.write(f"Selected Door Size: {door_size}")
#st.write("Base Price:" + doorprice)

st.divider()

st.write("Step 2: Select Hinge Type")
hinge_type = st.radio("", ["Left hinge", "Right hinge"], horizontal = True)

st.divider()

st.write("Step 3: Select hardware required")

mandatory_flags = {}
# currently hard-coded because there are no 'mandatory' labels in dataset
mandatory_categories = ["Mortice Locks ", "Interior handles", "Latch", "Machine Block"]

### need review!! door type can be examined here but we need to adopt csv as input
if door_type in door_prices[door_size]:
    # Add conditional hardware options based on door type
    HW_prices = getHWPrice(df1, door_type)

    total_price = float(doorprice.replace('$', '').replace(',', '').strip())

    for category, items in HW_prices.items():
        # Create a selection box for each category
        selected_item = st.selectbox(f"Select {category}:", list(items.keys()))

        if category in mandatory_categories:
            mandatory_flags[category] = selected_item != "Select an option..."
    
        # Add the price of the selected item
        if selected_item != "Select an option..." and items[selected_item] is not None:
            price_str = items[selected_item].strip().replace('$', '').replace(',', '')
            price = float(price_str)
            total_price += price
        #st.write(f"Price for {selected_item}: {price}")

st.divider()
# check flag
all_mandatory_filled = all(mandatory_flags.values())

total_price = float(total_price)
# only print total price if all mandatory fields are filled
if all_mandatory_filled:
    st.write(f"### Total Price: ${total_price:.2f}")
else:
    st.write("### Please complete all mandatory selections to see the total price.")

holder = ["Mortice:","Latch Plate:","Custom Latch Block:", "Exterior Plate/ Handle:", "Interior Plate/ Handle:", "Additional Hardware:"]

