import pandas as pd
import io, requests, json, uuid

df = pd.read_csv("C:\\Users\\SHUKLAK\\Desktop\\data.csv")
for index, row in df.iterrows():
    print(df.values)