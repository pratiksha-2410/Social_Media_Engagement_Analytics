# import Labraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset

df = pd.read_csv("social_media_engagement_advanced.csv")
print(df.head())

# Data Featuring

print("\n Data Shape:",df.shape)
print("\n Data Size:",df.size)
print("\n Data info:",df.info())
print("\n Data Describtion:",df.describe())

# Data Cleaning

print("\n Null values:",df.isna().sum())

# Find Duplicate Values & Remove them

print("\n Duplicate Values:",df.duplicated().sum())
print("\n",df.drop_duplicates())
