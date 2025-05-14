# suicide_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.set_page_config(page_title="Suicide Rate Analysis Dashboard", layout="centered")

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("who_suicide_statistics.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filter")
selected_year = st.sidebar.selectbox("Select Year",sorted(df['year'].unique()))
selected_country = st.sidebar.selectbox("Select Country",  sorted(df['country'].unique()))

# Filter data
if selected_country != "All":
    filtered_df = df[(df['year'] == selected_year) & (df['country'] == selected_country)]
else:
    filtered_df = df[df['year'] == selected_year]

# Title
st.title("📊 Suicide Rate Analysis Dashboard")
Worldwide_yearly_suicides = df[df['year'] == selected_year]['suicides_no'].sum()

#Total number of suicides in specific year
st.markdown(
     f"<h3>Worldwide suicide count for the year {selected_year} : <span style='color:red; font-weight:bold; font-size : 60px;'>{int(Worldwide_yearly_suicides):,}</span><br>",
    unsafe_allow_html=True
)

#find overall suicides in a country in a specific year
country_yearly_suicides = filtered_df['suicides_no'].sum()

if country_yearly_suicides == 0:
    st.markdown(
        f"<h4 style='color:gray;'>🟢 No suicides reported in {selected_country} in {selected_year}.</h4>",
        unsafe_allow_html=True
    )
else : 
    #📄 Data Snapshot
    st.subheader(f"📄 Data Snapshot: {selected_year} in {selected_country}")
    st.dataframe(filtered_df, use_container_width=True)

# Visualization 1: Suicide Rate by Gender
    st.subheader(f"Average Suicide Rate by Gender")
    gender_plot = filtered_df.groupby('sex')['suicides_no'].mean().reset_index()
    fig1 = sns.barplot(data=gender_plot, x='sex', y='suicides_no')
    st.pyplot(fig1.figure)
    plt.clf()

# Visualization 2: Average Suicide Rate by Age
    st.subheader("Average Suicide Rate by Age Group")
    age_plot = filtered_df.groupby('age')['suicides_no'].mean().reset_index()
    fig2 = sns.barplot(data=age_plot, x='age', y='suicides_no')
    plt.xticks(rotation=45)
    st.pyplot(fig2.figure)
    plt.clf()


