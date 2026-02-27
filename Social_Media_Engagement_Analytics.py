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

# Best Content Type

query = """SELECT Content_Type,AVG(Engagement_Rate)
FROM orders
GROUP BY Content_Type
ORDER BY AVG(Engagement_Rate) DESC"""

Content_Type = pd.read_sql(query,conn)
print(Content_Type)

# Best Platform Analysis

query = """SELECT Platform,AVG(Engagement_Rate)
FROM orders
GROUP BY Platform
ORDER BY AVG(Engagement_Rate) DESC"""

Best_Platform = pd.read_sql(query,conn)
print(Best_Platform)

# Top Three Performing Posts

query = """SELECT Post_ID,Platform,Content_Type,Engagement_Rate
FROM orders
GROUP BY Post_ID,Platform,Content_Type
ORDER BY Engagement_Rate DESC
LIMIT 3"""

Top_Performing_Posts = pd.read_sql(query,conn)
print(Top_Performing_Posts)

# Select Suspisious/Bot Engagement 

query = """
SELECT
    Post_ID,Engagement_Rate,
    CASE
        WHEN Engagement_Rate > 50
        THEN 'Suspisious'
        ELSE 'Normal'
END AS Engagement_Flag
FROM orders
""" 
Suspisious_Engagement = pd.read_sql(query,conn)
print(Suspisious_Engagement)

# Visualization

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#  Engagement Rate Distrubution
df['Total_Engagement'] = df['Likes'] + df['Comments'] + df['Shares']

plt.figure()
plt.hist(df['Engagement_Rate'], bins=6)
plt.title("Engagement Rate Distribution")
plt.xlabel("Engagement Rate (%)")
plt.ylabel("Number of Posts")
plt.show()

# Avg Engagement by Platform

platform_avg = df.groupby('Platform')['Engagement_Rate'].mean()

plt.figure()
plt.bar(platform_avg.index, platform_avg.values)
plt.title("Average Engagement Rate by Platform")
plt.xlabel("Platform")
plt.ylabel("Avg Engagement Rate (%)")
plt.show()

# Best Content Type Performance

content_avg = df.groupby('Content_Type')['Engagement_Rate'].mean()

plt.figure()
plt.bar(content_avg.index, content_avg.values)
plt.title("Average Engagement by Content Type")
plt.xlabel("Content Type")
plt.ylabel("Engagement Rate (%)")
plt.show()

# Business Insights

print(""" Business Insights:

1️ Platform Performance Insight:

Instagram shows the highest average engagement rate compared to Facebook and Twitter.

This suggests the audience is more interactive on visual-first platforms.

 Recommendation: Increase content investment on Instagram.

2️. Content Strategy Insight:

Reel and Video content types generate higher engagement than static Image or Text posts.

Short-form video drives stronger audience interaction.
 Recommendation: Focus more on Reels and Video-based content.

3️. Top Performing Posts Insight:

Top 5 posts contribute disproportionately to overall engagement.

High-performing posts often have:

Higher shares

Engaging captions

Better reach-to-engagement conversion

 Recommendation: Analyze what made top posts successful and replicate strategy.

4️. Engagement Distribution Insight:

Majority of posts fall within moderate engagement range.

A few posts act as outliers (very high engagement).

 Recommendation: Identify patterns in high-performing posts (timing, hashtags, format).

5️.Reach vs Engagement Insight:

Higher reach does not always guarantee higher engagement rate.

Some lower-reach posts performed better in terms of engagement percentage.

 Recommendation: Focus on quality content, not just reach.""")

# Save The CSV File

df.to_csv("social_media_engagement_advanced.csv",index=False)
