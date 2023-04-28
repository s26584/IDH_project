import pandas as pd

df = pd.read_csv('Food_Inspections.csv')


df['Inspection Date'] = pd.to_datetime(df['Inspection Date'])
df['Day'] = df['Inspection Date'].dt.day
df['Month'] = df['Inspection Date'].dt.month
df['Year'] = df['Inspection Date'].dt.year
df['DayOfTheWeek'] = df['Inspection Date'].dt.day_name()

df.to_csv('Food_Inspections_r.csv', index=False)