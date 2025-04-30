import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel("GirlsNamesDataset.xlsx")

df1 = pd.read_excel("GirlsNamesDataset.xlsx", sheet_name= "Table_1")
df2 = pd.read_excel("GirlsNamesDataset.xlsx", sheet_name= "Table_2")
df3 = pd.read_excel("GirlsNamesDataset.xlsx", sheet_name= "Table_3")
df4 = pd.read_excel("GirlsNamesDataset.xlsx", sheet_name= "Table_4")
df5 = pd.read_excel("GirlsNamesDataset.xlsx", sheet_name= "Table_5")
df6 = pd.read_excel("GirlsNamesDataset.xlsx", sheet_name= "Table_6")
df7 = pd.read_excel("GirlsNamesDataset.xlsx", sheet_name= "Table_7")
df8 = pd.read_excel("GirlsNamesDataset.xlsx", sheet_name= "Table_8")
st.title("Baby Names Dashboard")
st.markdown("*This interactive dashboard provied insights into the most popular baby names for girls in England and Wales. " \
            "You can explore trends overtime, compare regions, and use filters to interact with it. Use the visual charts and tables to understand how name preferences change across different age groups and months througout the year.*")
st.write("-------------------------------------------------------------------------------")

data_selection = st.selectbox("Choose the Data Set to Visualise", [
    "Home",
    "Top 100 Names (England & Wales)",
    "Top 100 Names by Country",
    "Top 10 Names by Region",
    "Top 10 Names by Month",
    "Overall Top Names",
    "Top Names by Area",
    "Top 100 by Mother's Age"
])
if data_selection == "Home":
    st.markdown("Below, you can see both a **Line Chart** and a **Bar Chart** representing the popularity of these names: " \
    "The **Line Chart** shows the trend of counts across names. " \
    "The **Bar Chart** provides a clearer comparison of the counts for each name.")
    st.snow()
    #For after please wait sign show those decided graphs
    with st.spinner("Please wait..."):
        time.sleep(5)
        st.subheader('Top 5 Baby Names')
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))  # 1 row, 2 columns
        names = ['Olivia', 'Amelia', 'Isla', 'Ava', 'Sophia']
        counts = [1000, 950, 900, 870, 860]
        ax1.plot(names, counts, marker='o')
        ax1.set_xlabel('Name')
        ax1.set_ylabel('Count')
        ax2.bar(names, counts)
        ax2.set_xlabel('Name')
        ax2.set_ylabel('Count')
        st.pyplot(fig)
    st.write("-------------------------------------------------------------------------------")
    st.subheader("Now add something else interactive")

elif data_selection == "Top 100 Names (England & Wales)":
    st.title("Baby Names Dashboard - England & Wales")
    st.subheader("Top 100 Baby Names (England & Wales, 2023)")
    top_names_df = df1.head(100)  # Top 100 names data
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(top_names_df['Name'], top_names_df['Count'])
    ax.set_title('Top 100 Baby Names (England & Wales, 2023)')
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75)  # Rotate x-axis labels for better readability
    st.pyplot(fig)
    st.write("The top 100 baby girls names in England & Wales offer insights into cultural shifts, parental preferences, and regional popularity. " \
    "Also, many names consistently remain in the top ranks year after year, other names have seen a surge in popularity or have just entered the top 100")
    st.write("As seen from the bar chart, **Olivia** continues to dominate as the most popular name, holding its place at the top of the list in 2023. " \
    "On the other hand, names like **Jasmine** and **Raya** are less frequently, meaning that their rankings are near the bottom. " \
    "However, they still highlight the diverse and unique choices parents are making for the names of their baby girls.")
# Page 2: Top 100 Names by Country (England vs Wales)
elif data_selection == "Top 100 Names by Country":
    st.title("Baby Names Dashboard - England & Wales")
    st.subheader("Top 100 Baby Names (England & Wales, 2023)")
    country = st.selectbox("Select Country", ["England", "Wales"])
    if country == "England":
        country_df = df2.head(100)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.bar(country_df['Name'], country_df['Count'])
        ax.set_title('Top 100 Baby Names in England 2023)')
        ax.set_xlabel('Name')
        ax.set_ylabel('Count')
        plt.xticks(rotation=75)  # Rotate x-axis labels for better readability
        st.pyplot(fig)
    else:
        country_df = df3.head(100)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.bar(country_df['Name'], country_df['Count'])
        ax.set_title(f"Top 100 Names in {country} (2023)")
        ax.set_xlabel('Name')
        ax.set_ylabel('Count')
        plt.xticks(rotation=75)
        st.pyplot(fig)

# Page 3: Top 10 Names by Region
elif data_selection == "Top 10 Names by Region":
    st.subheader("Top 10 Names by Region (England & Wales, 2023)")
    region = st.selectbox("Select Region", df4['Region'].unique())
    region_df = df4[df4['Region'] == region]
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(region_df['Name'], region_df['Count'])
    ax.set_title(f"Top 10 Names in {region} (2023)")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75)
    st.pyplot(fig)

# Page 4: Top 10 Names by Month
elif data_selection == "Top 10 Names by Month":
    st.subheader("Top 10 Names by Month of Birth (England & Wales, 2023)")
    month = st.selectbox("Select Month", df5['Month'].unique())
    month_df = df5[df5['Month'] == month]
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(month_df['Name'], month_df['Count'])
    ax.set_title(f"Top 10 Names in {month} (2023)")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75)
    st.pyplot(fig)

# Page 5: Overall Top Names
elif data_selection == "Overall Top Names":
    st.subheader("Overall Top Names (England & Wales, 2023)")
    overall_df = df6.head(100)  # Overall top names
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(overall_df['Name'], overall_df['Count'])
    ax.set_title("Top 100 Names (Overall)")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75)
    st.pyplot(fig)

# Page 6: Most Popular by Area
elif data_selection == "Top Names by Area":
    st.subheader("Most Popular Name by Area (England & Wales, 2023)")
    area_df = df7.head(10)  # Top names by area
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(area_df['Top Name'], area_df['Count'])
    ax.set_title("Most Popular Name by Area")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75)
    st.pyplot(fig)

# Page 7: Top 100 by Mother's Age
# Fix this page the age is not name, it is rank
elif data_selection == "Top 100 by Mother's Age":
    st.subheader("Top 100 Names by Mother's Age Group (England & Wales, 2023)")
    age_group = st.selectbox("Select Mother's Age Group", df8['AgeGroup'].unique())
    age_group_df = df8[df8['AgeGroup'] == age_group]
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(age_group_df['Name'], age_group_df['Count'])
    ax.set_title(f"Top 100 Names for Mother's Age Group: {age_group}")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75)
    st.pyplot(fig)
