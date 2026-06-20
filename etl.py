import pandas as pd

df = pd.read_csv("./Data/hotel_bookings.csv")

#print(df.shape)
#print(df.info())
#print(df.head())

#print(df.duplicated().sum())
#print(df.nunique())
#print(df.describe())
#print(df.isna().sum())

print(df.drop_duplicates().shape)