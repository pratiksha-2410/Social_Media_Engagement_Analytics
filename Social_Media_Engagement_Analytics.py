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


