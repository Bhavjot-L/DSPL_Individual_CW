import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import altair as alt

df = pd.read_excel("GirlsNamesDataset.xlsx")

df1 = pd.read_excel("GirlsNamesDataset.xlsx", sheet_name= "Table_1") #keep notes of the df's 
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

st.sidebar.title("Navigation")
st.sidebar.title("Select Data for Analysis")
data_selection = st.sidebar.radio("Choose the Data Set to Visualise", [
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
        counts = [2906, 2663, 2337, 2290, 2086]
        ax1.plot(names, counts, marker='o')
        ax1.set_xlabel('Name')
        ax1.set_ylabel('Count')
        ax2.bar(names, counts)
        ax2.set_xlabel('Name')
        ax2.set_ylabel('Count')
        st.pyplot(fig)
    st.write("-------------------------------------------------------------------------------")
    st.subheader("Now add the least 5 names")

elif data_selection == "Top 100 Names (England & Wales)":
    st.title("Baby Names - England & Wales")
    st.subheader("Top 100 Baby Names (England & Wales, 2023)")
    top_n = st.selectbox("Select number of top name to display in the bar chart:", options = [10,20,50,100])
    filtered_df = df.head(top_n)
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(filtered_df['Name'], filtered_df['Count'])
    ax.set_title('Top 100 Baby Names (England & Wales, 2023)')
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75, fontsize = 10)  # Rotate x-axis labels for better readability
    st.pyplot(fig)
    st.caption("You can zoom in for better view of the graph")    
    st.write("The top baby girls names in England & Wales offer insights into cultural shifts, parental preferences, and regional popularity. " \
    "Also, many names consistently remain in the top ranks year after year, other names have seen a surge in popularity or have just entered the top 100.")
    st.write("As seen from the bar chart, from the top 100 baby names, **Olivia** continues to dominate as the most popular name, holding its place at the top of the list in 2023. " \
    "On the other hand, names like **Jasmine** and **Raya** are less frequently, meaning that their rankings are near the bottom. " \
    "However, they still highlight the diverse and unique choices parents are making for the names of their baby girls.")
    st.info(f"The top {top_n} names have a total count of {filtered_df['Count'].sum():,} baby girls.")
    st.write("-------------------------------------------------------------------------------")

    #Line chart
    top_n_line = st.selectbox("Select number of top name to display in the Line chart:", options = [10,20,50,100], key = "line_chart_top_n") #to not clash with the bar chart
    filtered_line_df = df.head(top_n_line)
    fig2, ax2 = plt.subplots(figsize=(20, 10))
    ax2.plot(filtered_line_df['Name'], filtered_line_df['Count'], marker ='o')
    ax2.set_title(f'Top {top_n_line} Baby Names (England & Wales, 2023)')
    ax2.set_xlabel('Name')
    ax2.set_ylabel('Count')
    plt.xticks(rotation=75, fontsize = 14)  # Rotate x-axis labels for better readability
    st.pyplot(fig2)
    st.caption("You can zoom in for better view of the graph")
    st.write("The Line Chart shown above displayes the popularity of the top 100 baby girl names in England & Wales for the year 2023. " \
    "Each point in the chart represents a Name and the numebr of times it was given to the newborn baby girls.")
    st.write("This chart helps visualise how name usgae declines from the most popular to the less common ones, which is giving a clear picture of how name popularity is distributed. " \
    "Also, the name that is used the most becomes the most common name such as **Olivia** and the one that is least used such as **Raya** becomes more rare name for the baby.")
    st.info(f"The top {top_n_line} baby names have a total count of {filtered_line_df['Count'].sum():,} registrations.")
    st.write("-------------------------------------------------------------------------------")
    st.subheader("Total count of baby names:")
    total_count = df["Count"].sum()
    st.code(total_count)
    st.write("This is the total count of baby girl names that have been registered in England & Wales.")
    st.write("-------------------------------------------------------------------------------")
    st.write("The Dataset:")
    df
    st.write("As we can see from the table above, it represents the top 100 baby girl names registered in England and Wales, along with the number of times each name was used. " \
    "It also tracks how each name's popularity has shifted compared to both the previous year (2022) and the past decade (since 2013). " \
    "This allows us to spot any long-term trends, rising stars, and names that may be fading in popularity. For example, cultural influence, social media trends, and changing societal preferences.")

# Page 2: Top 100 Names by Country (England vs Wales)
elif data_selection == "Top 100 Names by Country":
    st.title("Baby Names - England & Wales")
    st.subheader("Top 100 Baby Names (England & Wales, 2023)")
    country = st.selectbox("Select your choice of Country", ["England", "Wales"])
    if country == "England": #MAKE SURE ITS DF2 FOR ENGLAND (they are different datasheets)
        top_n = st.selectbox("Select number of top name to display in the bar chart:", options = [10,20,50,100])
        filtered_df2 = df2.head(top_n)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.bar(filtered_df2['Name'], filtered_df2['Count'])
        ax.set_title('Top 100 Baby Names (England & Wales, 2023)')
        ax.set_xlabel('Name')
        ax.set_ylabel('Count')
        plt.xticks(rotation=75, fontsize = 12)  # Rotate x-axis labels for better readability
        st.pyplot(fig)
        st.info(f"The top {top_n} names have a total count of {filtered_df2['Count'].sum():,} baby girls.")
        #Line chart for England
        top_n_line = st.selectbox("Select number of top name to display in the Line chart:", options = [10,20,50,100], key = "line_chart_top_n") #to not clash with the bar chart        
        filtered_line_df2 = df2.head(top_n_line)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(filtered_line_df2['Name'], filtered_line_df2['Rank in England'], label= "England", marker ='o', color= 'blue')
        ax.plot(filtered_line_df2['Name'], filtered_line_df2['Rank in Wales'], label= "Wales",  marker ='o', color= 'orange')
        ax.set_title(f'Top {top_n_line} Baby Names (England & Wales, 2023)')
        ax.set_xlabel('Name', fontsize = 16)
        ax.set_ylabel('Rank (Lower is Better)', fontsize= 16)
        ax.invert_yaxis()
        ax.legend()
        plt.xticks(rotation=75, fontsize = 14)  # Rotate x-axis labels for better readability
        st.pyplot(fig)
        st.info(f"The top {top_n_line} baby names have a total count of {filtered_line_df2['Count'].sum():,} registrations.")
        st.write("This section compares the popularity of baby girl names between England and Wales in 2023. " \
        "The chart above shows how each name ranks in both countries, helping us identify names that are mostly used across the regions. " \
        "Also, A lower rank (closer to 1) means higher popularity. Using the line chart, we can spot patterns such as names that are top ranked in Wales but less common in England, and vice versa.")
        #scatter chart
       # top_n_scatter = st.selectbox("Select number of top name to display in the Scatter chart:", options = [10,20,50,100])
        scatter_df = df2.head(100) #change 100 to ton_n_scatter if adding that option
        chart = alt.Chart(scatter_df).mark_circle().encode(
            x="Rank in England",
            y="Rank in Wales",
            tooltip=["Name","Rank in England","Rank in Wales"]
        ).properties(
            title=f"England vs Wales Rank Comparison"
        )
        st.altair_chart(chart, use_container_width=True)
        st.write("This scatter plot shows how the names rank in England compared to Wales. If a name is equally popular in both places, it will be near the diagonal line. Hover to see more details about each name.")
        st.write("-------------------------------------------------------------------------------")
    else: #MAKE SURE IT'S DF3 FOR WALES
        top_n = st.selectbox("Select number of top name to display in the bar chart:", options = [10,20,50,100])
        filtered_df3 = df3.head(top_n)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.bar(filtered_df3['Name'], filtered_df3['Count'])
        ax.set_title('Top 100 Baby Names (England & Wales, 2023)')
        ax.set_xlabel('Name')
        ax.set_ylabel('Count')
        plt.xticks(rotation=75, fontsize = 12)  # Rotate x-axis labels for better readability
        st.pyplot(fig)
        st.info(f"The top {top_n} names have a total count of {filtered_df3['Count'].sum():,} baby girls.")
        top_n_line = st.selectbox("Select number of top name to display in the Line chart:", options = [10,20,50,100], key = "line_chart_top_n") #to not clash with the bar chart        
        filtered_line_df3 = df3.head(top_n_line)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(filtered_line_df3['Name'], filtered_line_df3['Rank in Wales'], label= "Wales", marker ='o', color= 'orange')
        ax.plot(filtered_line_df3['Name'], filtered_line_df3['Rank in England'], label= "England",  marker ='o', color= 'blue')
        ax.set_title(f'Top {top_n_line} Baby Names (England & Wales, 2023)')
        ax.set_xlabel('Name', fontsize = 16)
        ax.set_ylabel('Rank (Lower is Better)', fontsize= 16)
        ax.invert_yaxis()
        ax.legend()
        plt.xticks(rotation=75, fontsize = 14)  # Rotate x-axis labels for better readability
        st.pyplot(fig)
        st.info(f"The top {top_n_line} baby names have a total count of {filtered_line_df3['Count'].sum():,} registrations.")
        st.write("This section also compares the popularity of baby girl names between Wales and England in 2023. " \
        "The chart above shows how each name ranks in both countries, helping us identify names that are mostly used across the regions. " \
        "Also, A lower rank (closer to 1) means higher popularity. Using the line chart, we can spot patterns such as names that are top ranked in England but less common in Wales, and vice versa.")
        #scatter chart
       # top_n_scatter = st.selectbox("Select number of top name to display in the Scatter chart:", options = [10,20,50,100])
        scatter_df3 = df3.head(100) #change 100 to ton_n_scatter if adding that option
        chart = alt.Chart(scatter_df3).mark_circle().encode(
            x="Rank in Wales",
            y="Rank in England",
            tooltip=["Name","Rank in Wales","Rank in England"]
        ).properties(
            title=f"Wales vs England Rank Comparison"
        )
        st.altair_chart(chart, use_container_width=True)
        st.write("This scatter plot shows how the names rank in Wales compared to England. Hover to see more details about each name.")
        st.write("-------------------------------------------------------------------------------")

# Page 3: Top 10 Names by Region
elif data_selection == "Top 10 Names by Region":
    st.subheader("Top 10 Names by Region (England & Wales, 2023)")
    top10_df = df4[df4['Name'] != 'All Names']
    region = st.selectbox("Select Region", df4['Geography'].unique())
    region_df = top10_df[top10_df['Geography'] == region]
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(region_df['Name'], region_df['Count'])
    ax.set_title(f"Top 10 Names in {region} (2023)")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75)
    st.pyplot(fig)
    total_all_names = df4[df4['Name'] == 'All Names']['Count'].sum()
    st.write("This chart highlights the top 10 most popular baby names in each region, giving a clear view of naming trends across England & Wales.")    
    st.info(f"Across all regions, the total number of baby name registrations (all names combined) is **{total_all_names:,}**.")
    st.write("-------------------------------------------------------------------------------")
    data = {
    'Region': ['North East', 'North West', 'Yorkshire And The Humber', 'East Midlands', 'West Midlands', 'East Of England', 'London', 'South East', 'South West', 'Wales'],
    'Count': [11944, 35710, 26446, 22401, 30114, 30856, 50932, 42929, 23227, 13409]
    }
    df4_data = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.pie(df4_data['Count'], labels=df4_data['Region'], startangle=90)
    ax.axis('equal')
    ax.set_title("Distribution of Top Baby Names By Region (England & Wales)", fontsize = 16)
    st.pyplot(fig)
    st.write("This pie chart shows how the total number of baby name registrations is split across each region in England & Wales.")
    st.write("-------------------------------------------------------------------------------")

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
