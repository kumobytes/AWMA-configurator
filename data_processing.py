import pandas as pd

df = pd.read_csv("Door_prices.csv")

def convert_currency(value):
    return float(value.replace('$', '').replace(',', ''))

def cleanBasePriceData(df):
    df = df.drop(["DoorSizeID", "Description",
                  "DateEntered","Height","Width","Thickness"], axis=1)
    df['amount'] = df[' UnitSell '].apply(convert_currency)
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

test = getBasePrice(df)
print(test)