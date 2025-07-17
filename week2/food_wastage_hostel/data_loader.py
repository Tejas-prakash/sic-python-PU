import pandas as pd

def load_data():
    path = "hostel_food_wastage_large.xlsx.csv"
    df = pd.read_csv(path)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Wasted_Percentage'] = (df['Total_Food_Wasted_kg'] / df['Food_Prepared_kg']) * 100
    return df
