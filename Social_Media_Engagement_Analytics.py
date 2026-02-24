# import Labraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Database Connection

conn = sqlite3.connect("social_media.db")
cursor = conn.cursor()

# Load Dataset

df = pd.read_csv("social_media_engagement_advanced.csv")
df.to_sql("orders",conn,if_exists="replace",index=False)
print(df.head())

# Data Featuring

print("\n Data Shape:",df.shape)
print("\n Data Size:",df.size)
print("\n Data info:",df.info())
print("\n Data Describtion:",df.describe())
print(df.columns)

# Data Cleaning

print("\n Null values:",df.isna().sum())

# Finding Duplicate Values & Remove them

print("\n Duplicate Values:",df.duplicated().sum())
print("\n",df.drop_duplicates())

#  Rename Column

df.rename(columns={"Engagement_Rate (%)":"Engagement_Rate"},inplace=True)
df.to_sql("orders",conn,if_exists="replace",index=False)

# Max Engagement Post_ID via Pandas
max_index = df["Engagement_Rate"].idxmax()
max_post_ID = df.loc[max_index,"Post_ID"]
max_engagement_rate = df.loc[max_index,"Engagement_Rate"]

print("Post with Highest Engagement")
print("Post_ID",max_post_ID)
print("Engagement_Rate",max_engagement_rate )

# Max Engagement Post_ID via SQL

query = """SELECT Post_ID,Engagement_Rate 
FROM orders
WHERE Engagement_Rate = (SELECT MAX(Engagement_Rate)
FROM orders)""" 

Max_Post_ID = pd.read_sql(query,conn)
print(Max_Post_ID)


