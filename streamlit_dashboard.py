import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np
import altair as alt

df = pd.read_excel("Data Files\GirlsNamesDataset.xlsx")

df1 = pd.read_excel("Data Files\GirlsNamesDataset.xlsx", sheet_name= "Table_1") #keep notes of the df's 
df2 = pd.read_excel("Data Files\GirlsNamesDataset.xlsx", sheet_name= "Table_2") # Reading each file SHEET seperately
df3 = pd.read_excel("Data Files\GirlsNamesDataset.xlsx", sheet_name= "Table_3")
df4 = pd.read_excel("Data Files\GirlsNamesDataset.xlsx", sheet_name= "Table_4")
df5 = pd.read_excel("Data Files\GirlsNamesDataset.xlsx", sheet_name= "Table_5")
df6 = pd.read_excel("Data Files\GirlsNamesDataset.xlsx", sheet_name= "Table_6")
df7 = pd.read_excel("Data Files\GirlsNamesDataset.xlsx", sheet_name= "Table_7")
df8 = pd.read_excel("Data Files\GirlsNamesDataset.xlsx", sheet_name= "Table_8")
st.title("Baby Names Dashboard")                                        # The top Home page for all
st.markdown("*This interactive dashboard provied insights into the most popular baby names for girls in England and Wales. " \
            "You can explore trends overtime, compare regions, and use filters to interact with it. Use the visual charts and tables to understand how name preferences change across different age groups and months througout the year.*")
st.write("-------------------------------------------------------------------------------")

st.sidebar.title("Navigation")                  # Main Navigation on the left
st.sidebar.title("Select Data for Analysis")
data_selection = st.sidebar.radio("Choose the Data to Visualise", [
    "Dashboard", "Top Names (England & Wales)", "Top Names by Country", "Top 10 Names by Region", 
    "Top 10 Names by Month", "Overall Top Names", "Top Names by Area", "Top 100 by Mother's Age"
])
if data_selection == "Dashboard":                            # Necessary coding because there are 8 Pages. Use IF for it
    st.markdown("Below, you can see both a **Line Chart** and a **Bar Chart** representing the popularity of these names: " \
    "The **Line Chart** shows the trend of counts across names. " \
    "The **Bar Chart** provides a clearer comparison of the counts for each name. " \
    "The **Scatter Chart** shows relationships of Baby Names between England & Wales.")
    st.snow()           #Just an interactive feature you can change it to balloons
    with st.spinner("Please wait..."):
        time.sleep(5)
        st.subheader("Top 10 Names (England & Wales)")
        summary_df = df.head(10)
        fig, ax = plt.subplots(figsize=(20, 10)) #The main start of the graphs 
        ax.bar(summary_df['Name'], summary_df['Count'])
        ax.set_title('Top 10 Baby Names (England & Wales, 2023)')
        ax.set_xlabel('Name')
        ax.set_ylabel('Count')
        plt.xticks(rotation=75, fontsize = 14)  #Rotate x-axis number used in rotation for better readability
        st.pyplot(fig)
        st.write("-------------------------------------------------------------------------------")
        st.subheader("Bottom 10 Baby names (England & Wales)")
        fig, ax, = plt.subplots(figsize=(12, 6))  
        bar_names = ['Hazel', 'Darcie', 'Lara', 'Hannah', 'Lilah', 'Autumn', 'Nellie', 'Jasmine', 'Navaeh', 'Raya']
        bar_counts = [527, 525, 525, 515, 513, 510, 509, 501, 494, 486]
        ax.bar(bar_names, bar_counts)
        ax.set_title("Bottom 10 Baby Names (England & Wales)")
        ax.set_xlabel('Name')
        ax.set_ylabel('Count')
        st.pyplot(fig)
        st.write("-------------------------------------------------------------------------------")
        st.subheader("Name Rank in England vs Wales")
        summary_line_df = df2.head(10)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(summary_line_df['Name'], summary_line_df['Rank in England'], label= "England", marker ='o', color= 'blue')
        ax.plot(summary_line_df['Name'], summary_line_df['Rank in Wales'], label= "Wales",  marker ='o', color= 'orange')
        ax.set_title('Rank Comparison (Lower is Better)')
        ax.set_xlabel('Name', fontsize = 16)
        ax.set_ylabel('Rank (Lower is Better)', fontsize= 16)
        ax.invert_yaxis()
        ax.legend()
        plt.xticks(rotation=75, fontsize = 14)
        st.pyplot(fig)
        st.write("-------------------------------------------------------------------------------")
        summary_scatter_df = df2.head(100)
        chart = alt.Chart(summary_scatter_df).mark_circle().encode(
            x="Rank in England",
            y="Rank in Wales",
            tooltip=["Name","Rank in England","Rank in Wales"]
        ).properties(                                   # This is just to add a title for the graph
            title=f"England vs Wales Rank Comparison"
        )
        st.altair_chart(chart, use_container_width=True)
        st.write("-------------------------------------------------------------------------------")

elif data_selection == "Top Names (England & Wales)": #England and Wales combines (Together)
    st.title("Baby Names - England & Wales")
    st.subheader("Top Baby Names (England & Wales, 2023)")
    top_n = st.selectbox("Select number of top name to display in the bar chart:", options = [10,25,50,75,100]) #Giving the user a selection
    filtered_df = df.head(top_n)
    fig, ax = plt.subplots(figsize=(20, 10)) #The main start of the graphs 
    ax.bar(filtered_df['Name'], filtered_df['Count'])
    ax.set_title(f'Top {top_n} Baby Names (England & Wales, 2023)')
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75, fontsize = 10)  #Rotate x-axis number used in rotation for better readability
    st.pyplot(fig)
    st.caption("You can zoom in for better view of the graph")    
    st.write("The top baby girls names in England & Wales offer insights into cultural shifts, parental preferences, and regional popularity. Also, many names consistently remain in the top ranks year after year, other names have seen a surge in popularity or have just entered the top 100.")
    st.write("As seen from the bar chart, from the top 100 baby names, **Olivia** continues to dominate as the most popular name, holding its place at the top of the list in 2023. On the other hand, names like **Jasmine** and **Raya** are less frequently, meaning that their rankings are near the bottom. However, they still highlight the diverse and unique choices parents are making for the names of their baby girls.")
    st.info(f"The top {top_n} names have a total count of {filtered_df['Count'].sum():,} baby girls.")
    st.write("-------------------------------------------------------------------------------")
    # Line chart
    top_n_line = st.selectbox("Select number of top name to display in the Line chart:", options = [10,25,50,75,100], key = "line_chart_top_n") #to not clash with the bar chart
    filtered_line_df = df.head(top_n_line)
    fig2, ax2 = plt.subplots(figsize=(20, 10))
    ax2.plot(filtered_line_df['Name'], filtered_line_df['Count'], marker ='o')
    ax2.set_title(f'Top {top_n_line} Baby Names (England & Wales, 2023)')
    ax2.set_xlabel('Name')
    ax2.set_ylabel('Count')
    plt.xticks(rotation=75, fontsize = 14)
    st.pyplot(fig2)
    st.caption("You can zoom in for better view of the graph")
    st.write("The Line Chart shown above displayes the popularity of the top 100 baby girl names in England & Wales for the year 2023. Each point in the chart represents a Name and the numebr of times it was given to the newborn baby girls.")
    st.write("This chart helps visualise how name usgae declines from the most popular to the less common ones, which is giving a clear picture of how name popularity is distributed. Also, the name that is used the most becomes the most common name such as **Olivia** and the one that is least used such as **Raya** becomes more rare name for the baby.")
    st.info(f"The top {top_n_line} baby names have a total count of {filtered_line_df['Count'].sum():,} registrations.")
    st.write("-------------------------------------------------------------------------------")
    st.subheader("Total count of baby names:")
    total_count = df["Count"].sum()
    st.code(total_count)
    st.write("This is the total count of baby girl names that have been registered in England & Wales.")
    st.write("-------------------------------------------------------------------------------")
    st.write("The Dataset:")
    df
    st.write("As we can see from the table above, it represents the top 100 baby girl names registered in England and Wales, along with the number of times each name was used. It also tracks how each name's popularity has shifted compared to both the previous year (2022) and the past decade (since 2013). This allows us to spot any long-term trends, rising stars, and names that may be fading in popularity. For example, cultural influence, social media trends, and changing societal preferences.")

# Page 2: Top Names by Country (England vs Wales)
elif data_selection == "Top Names by Country":
    st.title("Baby Names - England & Wales")
    country = st.radio("Select your choice of Country", ["England", "Wales"])
    if country == "England": #MAKE SURE ITS DF2 FOR ENGLAND (they are different datasheets)
        st.subheader("Baby Names (England, 2023)")
        top_n = st.selectbox("Select number of top name to display in the bar chart:", options = [10,25,50,75,100])
        filtered_df2 = df2.head(top_n)                          # The formula for graphs and charts are pretty much the same except the small changes like variables names
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.bar(filtered_df2['Name'], filtered_df2['Count'])
        ax.set_title(f'Top {top_n} Baby Names (England & Wales, 2023)')
        ax.set_xlabel('Name')
        ax.set_ylabel('Count')
        plt.xticks(rotation=75, fontsize = 12)
        st.pyplot(fig)
        st.info(f"The top {top_n} names have a total count of {filtered_df2['Count'].sum():,} baby girls.")
        #Line chart for England
        top_n_line = st.selectbox("Select number of top name to display in the Line chart:", options = [10,25,50,75,100], key = "line_chart_top_n") #to not clash with the bar chart        
        filtered_line_df2 = df2.head(top_n_line)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(filtered_line_df2['Name'], filtered_line_df2['Rank in England'], label= "England", marker ='o', color= 'blue')
        ax.plot(filtered_line_df2['Name'], filtered_line_df2['Rank in Wales'], label= "Wales",  marker ='o', color= 'orange')
        ax.set_title(f'Top {top_n_line} Baby Names (England & Wales, 2023)')
        ax.set_xlabel('Name', fontsize = 16)
        ax.set_ylabel('Rank (Lower is Better)', fontsize= 16)
        ax.invert_yaxis()
        ax.legend()
        plt.xticks(rotation=75, fontsize = 14)
        st.pyplot(fig)
        st.info(f"The top {top_n_line} baby names have a total count of {filtered_line_df2['Count'].sum():,} registrations.")
        st.write("This section compares the popularity of baby girl names between England and Wales in 2023. The chart above shows how each name ranks in both countries, helping us identify names that are mostly used across the regions. Also, A lower rank (closer to 1) means higher popularity. Using the line chart, we can spot patterns such as names that are top ranked in Wales but less common in England, and vice versa.")
        #scatter chart
        scatter_df = df2.head(100)
        chart = alt.Chart(scatter_df).mark_circle().encode(
            x="Rank in England",
            y="Rank in Wales",
            tooltip=["Name","Rank in England","Rank in Wales"]
        ).properties(                                   # This is just to add a title for the graph
            title=f"England vs Wales Rank Comparison"
        )
        st.altair_chart(chart, use_container_width=True)
        st.write("This scatter plot shows how the names rank in England compared to Wales. If a name is equally popular in both places, it will be near the diagonal line. Hover to see more details about each name.")
        st.write("-------------------------------------------------------------------------------")
    else: #MAKE SURE IT'S DF3 FOR WALES
        st.subheader("Baby Names (Wales, 2023)")
        top_n = st.selectbox("Select number of top name to display in the bar chart:", options = [10,25, 50, 75, 100])
        filtered_df3 = df3.head(top_n)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.bar(filtered_df3['Name'], filtered_df3['Count'])
        ax.set_title(f'Top {top_n} Baby Names (England & Wales, 2023)')
        ax.set_xlabel('Name')
        ax.set_ylabel('Count')
        plt.xticks(rotation=75, fontsize = 12)
        st.pyplot(fig)
        st.info(f"The top {top_n} names have a total count of {filtered_df3['Count'].sum():,} baby girls.")
        top_n_line = st.selectbox("Select number of top name to display in the Line chart:", options = [10, 25, 50, 75, 100], key = "line_chart_top_n") #to not clash with the bar chart        
        filtered_line_df3 = df3.head(top_n_line)
        fig, ax = plt.subplots(figsize=(20, 10))
        ax.plot(filtered_line_df3['Name'], filtered_line_df3['Rank in Wales'], label= "Wales", marker ='o', color= 'orange')
        ax.plot(filtered_line_df3['Name'], filtered_line_df3['Rank in England'], label= "England",  marker ='o', color= 'blue')
        ax.set_title(f'Top {top_n_line} Baby Names (England & Wales, 2023)')
        ax.set_xlabel('Name', fontsize = 16)
        ax.set_ylabel('Rank (Lower is Better)', fontsize= 16)
        ax.invert_yaxis()
        ax.legend()
        plt.xticks(rotation=75, fontsize = 14)
        st.pyplot(fig)
        st.info(f"The top {top_n_line} baby names have a total count of {filtered_line_df3['Count'].sum():,} registrations.")
        st.write("This section also compares the popularity of baby girl names between Wales and England in 2023. The chart above shows how each name ranks in both countries, helping us identify names that are mostly used across the regions. Also, A lower rank (closer to 1) means higher popularity. Using the line chart, we can spot patterns such as names that are top ranked in England but less common in Wales, and vice versa.")
        #scatter chart
        scatter_df3 = df3.head(100) 
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
elif data_selection == "Top 10 Names by Region":            # Now seperating it by regions
    st.subheader("Top 10 Names by Region (England & Wales, 2023)")
    top10_df = df4[df4['Name'] != 'All Names']                     # Filtering 'All names' out so it does not make the graph look weird, so it takes only the names part 
    region = st.selectbox("Select Region", df4['Geography'].unique())           #Only reading the regions by Geography (locations)
    region_df = top10_df[top10_df['Geography'] == region]
    fig, ax = plt.subplots(figsize=(20, 10))                #Now the plot
    ax.bar(region_df['Name'], region_df['Count'])
    ax.set_title(f"Top 10 Names in {region} (2023)")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75)
    st.pyplot(fig)
    region_count = df4[(df4['Geography'] == region) & (df4['Name'] == 'All Names')]['Count'].values[0]          # Get the total number of baby name registrations for the selected region, where the name is 'All Names' (represents the total count across all names)
    st.info(f"Total baby name registrations in {region}: **{region_count:,}**.")
    total_all_names = df4[df4['Name'] == 'All Names']['Count'].sum()                    # Now for the total for All names 
    st.write("This chart highlights the top 10 most popular baby names in each region, giving a clear view of naming trends across England & Wales.")
    st.write("-------------------------------------------------------------------------------")
    data = {                                # I added the values manually for region wise for the count
    'Region': ['North East', 'North West', 'Yorkshire And The Humber', 'East Midlands', 'West Midlands', 'East Of England', 'London', 'South East', 'South West', 'Wales'],
    'Count': [11944, 35710, 26446, 22401, 30114, 30856, 50932, 42929, 23227, 13409]
    }
    df4_data = pd.DataFrame(data)
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.pie(df4_data['Count'], labels=df4_data['Region'], startangle=90, autopct='%1.1f%%')
    ax.axis('equal')
    ax.set_title("Distribution of Top Baby Names By Region (England & Wales)", fontsize = 16)
    st.pyplot(fig)
    st.write("This pie chart shows how the total number of baby name registrations is split across each region in England & Wales.")
    st.info(f"Across all regions, the total number of baby name registrations (all names combined) is **{total_all_names:,}**.")    
    st.write("-------------------------------------------------------------------------------")
    st.subheader("Map of Baby Name Counts by Region")
    st.write("This map shows the locations of regions in England & Wales, with each point representing the location of the total number of baby name registrations in that area.")
    data_map= {
        'Region': ['North East', 'North West', 'Yorkshire And The Humber', 'East Midlands', 'West Midlands', 'East Of England', 'London', 'South East', 'South West', 'Wales'],
        'Count': [11944, 35710, 26446, 22401, 30114, 30856, 50932, 42929, 23227, 13409],
        'lat': [54.7753, 53.7676, 53.9586, 52.9548, 52.4862, 52.3555, 51.5072, 51.2992, 51.4545, 52.1307],    #Used Google maps for these locations            
        'lon': [-1.5849, -2.7186, -1.0803, -1.1581, -1.8904, 1.1743, -0.1276, -0.5615, -2.5879, -3.7837]
    }
    df4_map = pd.DataFrame(data_map) 
    st.map(df4_map[['lat', 'lon']])

# Page 4: Top 10 Names by Month
elif data_selection == "Top 10 Names by Month":                 #Same procedure from Regions
    st.subheader("Top 10 Names by Month of Birth (England & Wales, 2023)")
    top10_df5 = df5[df5['Name'] != 'All names']    
    month = st.selectbox("Select Month", df5['Month'].unique())
    month_df = top10_df5[top10_df5['Month'] == month]
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(month_df['Name'], month_df['Count'])
    ax.set_title(f"Top 10 Names in {month} (2023)")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75, fontsize= 14)
    st.pyplot(fig)
    st.write("This bar chart presents the top 10 baby names for each month offering a clear comparison of the most popular names in any given month of the year.")
    month_count = df5[(df5['Name'] == 'All names')]['Count'].values[0]
    st.info(f"Total baby name registrations in {month}: **{month_count:,}**.")
    st.write("-------------------------------------------------------------------------------")
    top10pie_df5 = df5[df5['Name'] != 'All names']
    month_pie = st.selectbox("Select your choice of Month:", df5['Month'].unique())
    month_df5 = top10pie_df5[top10pie_df5['Month'] == month_pie]
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.pie(month_df5['Count'], labels=month_df5['Name'], startangle=90, autopct='%1.1f%%')
    ax.axis('equal')
    ax.set_title("Distribution of Top Baby Names By Region (England & Wales)", fontsize = 16)
    st.pyplot(fig)
    st.write("The Pie chart visualises the distribution of the total number of baby name registrations for a selected month.")
    st.write("This pie chart shows the top baby names and their percentage. For example, the use **Isabella** on January is 8.5 percent and **Olivia** is 13.3 percent. This means that during January the name **Olivia** is user more than **Isabella**. ")
    st.write("-------------------------------------------------------------------------------")
    top10line_df5 = df5[df5['Name'] != 'All names']
    fig, ax = plt.subplots(figsize=(20, 10)) # For loop to show the name trend between the months
    for name in top10line_df5['Name'].unique():
        name_df = top10line_df5[top10line_df5['Name'] == name]
        ax.plot(name_df['Month'], name_df['Count'], marker='o')
    ax.set_title("Trend of Baby Names in England & Wales")
    ax.set_xlabel('Month', fontsize=14)
    ax.set_ylabel('Count', fontsize=14)
    ax.legend() # Not showing/working for some reason
    st.pyplot(fig)          # This is to view the plot
    st.write("The Line Chart demonstrates the rise and fall of popularity for various baby names throughout the year, which highlights seasonal trends and many other changes.")
    st.write("-------------------------------------------------------------------------------")

# Page 5: Overall Top Names
elif data_selection == "Overall Top Names":
    st.subheader("Overall Top Names (England & Wales, 2023)")
    overall_df = df6.head(10)  # Overall top names
    st.markdown("This chart highlights the most commonly registered baby names across all regions and months combines.")
    fig, ax = plt.subplots(figsize=(20, 10))
    ax.bar(overall_df['Name'], overall_df['Count'])
    ax.set_title("Top 10 Names (Overall)")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75, fontsize = 14)
    st.pyplot(fig)
    st.info(f"There are total of **{len(df6):,}** baby name records.")
    st.write("-------------------------------------------------------------------------------")
    st.write("This is the dataset for all Names Registered in 2023.")    
    df6

# Page 6: Most Popular by Area
elif data_selection == "Top Names by Area":
    st.subheader("Most Popular Name by Area (England & Wales, 2023)")
    top_name_counts = df7['Top Name'].value_counts().reset_index()      # To count how many times each name is in the top in an area.
    top_name_counts.columns = ['Top Name', 'Count']
    area_df7 = top_name_counts.head(10)             # Now taking the top 10 most used names
    fig, ax = plt.subplots(figsize=(20, 10))        #Now ploting it
    ax.bar(area_df7['Top Name'], area_df7['Count'])
    ax.set_title("Most Popular Name Across All Areas")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75, fontsize = 14)
    st.pyplot(fig)
    st.write("This chart shows which girl names appear the most frequently as the top choice across areas.")
    st.write("-------------------------------------------------------------------------------")
    geography = st.radio("Select the Geography Type", df7['Geography type'].unique())       #This is to find the most common names by area or across all areas.
    geography_df = df7[df7['Geography type'] == geography]
    df7_grouped = geography_df.groupby(['Geography type', 'Area of usual residence name', 'Top Name'])['Count'].sum().reset_index()         # Grouping them so that we can then sum the count
    st.write(f"Total count per Area of usual residence name for {geography}:")
    st.write(df7_grouped)
    fig, ax = plt.subplots(figsize=(20, 10))                #Now the plot
    ax.bar(geography_df['Top Name'], geography_df['Count'])
    ax.set_title(f"Top Names in {geography} (2023)")
    ax.set_xlabel('Name')
    ax.set_ylabel('Count')
    plt.xticks(rotation=75)
    st.pyplot(fig)
    st.write("-------------------------------------------------------------------------------")

# Page 7: Top 100 by Mother's Age
# This page, the age is not name, it is rank
elif data_selection == "Top 100 by Mother's Age":
    st.subheader("Top Names by Mother's Age Group (England & Wales, 2023)")
    age_groups = {                      #Grouping the columns in a specific format and it will be used later on for allowing the user to select an option
    "Aged under 25": ["Aged under 25 Name", "Aged under 25 Rank"],
    "Aged 25 to 29": ["Aged 25 to 29 Name", "Aged 25 to 29 Rank"],
    "Aged 30 to 34": ["Aged 30 to 34 Name", "Aged 30 to 34 Rank"],
    "Age 35 and over": ["Age 35 and over Name", "Age 35 and over Rank"]
    }
    age_group = st.radio("Select an Age Group: ", list(age_groups.keys()))
    top_n_df8 = st.selectbox("Select the number of top names:", [10, 25, 50, 75, 100])
    name_df8, rank_df8 = age_groups[age_group]                  # To pick up the matching columns for the selected age group
    top_names = df8[[name_df8, rank_df8]].sort_values(by=rank_df8).head(top_n_df8)      # Now filtering the top names for the selected age group for the user.
    fig, ax = plt.subplots(figsize=(20, 10))                            # Now plotting the graph
    ax.bar(top_names[name_df8], top_names[rank_df8])
    ax.set_title(f"Top {top_n_df8} Names in Age Group: {age_group}")
    ax.set_xlabel('Name')
    ax.set_ylabel('Rank (Lower is Better)')
    plt.xticks(rotation=75)
    st.pyplot(fig)
    st.write("The Bar chart displays the ranking of names within the selected age group, showing how popular each name is based on its rank across different age ranges. ")
    st.write("-------------------------------------------------------------------------------")
    st.markdown("The table below shows ranked baby names across all Mother's Age Groups, it offers a clear view of how naming trends vary across generations. This can be useful to explore different trends and patterns.")
    df8
    st.write("-------------------------------------------------------------------------------")
