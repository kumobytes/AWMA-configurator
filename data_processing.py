import pandas as pd

df = pd.read_csv("Door_prices.csv")
df1 = pd.read_csv("Hardware_prices.csv", encoding="latin-1")

def convert_currency(value):
    return float(value.replace('$', '').replace(',', ''))

def cleanBasePriceData(df):
    df = df.drop(["DoorSizeID", "Description",
                  "DateEntered","Height","Width","Thickness"], axis=1)
    df['amount'] = df[' UnitSell '].apply(convert_currency)
    return df

def cleanHWPriceData(df):
    df = df.loc[:,["Applicable Door Type", "Hardware Type",
                  "Hardware description"," Unit Sell  "]]
    df['amount'] = df[' Unit Sell  '].apply(convert_currency)
    return df

def getBasePrice(df):
    df = cleanBasePriceData(df)
    door_prices = {}
    for index, row in df.iterrows():
        size = row['Size']
        price = row[' UnitSell ']
        door_type = row['ThicknessType']
        
        if size not in door_prices:
            door_prices[size] = {}  # Initialize nested dictionary
        
        door_prices[size][door_type] = price

    return door_prices

def getHWPrice(df):
    df = cleanHWPriceData(df)
    HW_prices = {}
    for index, row in df.iterrows():
        hardwareType = row['Hardware Type']
        price = row[' Unit Sell  ']
        desc = row['Hardware description']
        
        if hardwareType not in HW_prices:
            HW_prices[hardwareType] = {}

        HW_prices[hardwareType][desc] = price
    
    return HW_prices


test = getBasePrice(df)
print(test)