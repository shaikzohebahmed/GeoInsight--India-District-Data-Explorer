import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

# Load the data once at the beginning of the script to avoid reading it multiple times
df = pd.read_csv('india.csv')

# Create a list of unique states for the sidebar dropdown
list_of_states = ['Overall India'] + list(df['State'].unique())

# Set page layout to wide
st.set_page_config(layout='wide')

# Sidebar title
st.sidebar.title('India Data Explorer')

# Sidebar widgets
selected_states = st.sidebar.multiselect('Select States', list_of_states, default=['Overall India'])
primary_parameter = st.sidebar.selectbox('Select a Primary Parameter', sorted(df.columns[5:]))
secondary_parameter = st.sidebar.selectbox('Select a Secondary Parameter', sorted(df.columns[5:]))
plot = st.sidebar.button('Plot Graph')

# Main content
if plot:
    st.text('Size represents Primary parameter')
    st.text('Color represents Secondary parameter')
    
    if 'Overall India' in selected_states:
        filtered_df = df  # Use the entire dataset
    else:
        filtered_df = df[df['State'].isin(selected_states)]  # Filter by selected states
    
    # Create the scatter plot using Plotly Express
    fig = px.scatter_mapbox(
        filtered_df,
        lat="Latitude",
        lon="Longitude",
        color=secondary_parameter,
        size=primary_parameter,
        color_continuous_scale=px.colors.sequential.Plasma,
        size_max=35,
        zoom=4,
        mapbox_style="carto-positron",
        width=1200,
        height=700,
        hover_name='District'
    )
    
    # Display the plot in the Streamlit app
    st.plotly_chart(fig, use_container_width=True)

    # Data Summary
    st.header('Data Summary')
    st.write('Summary statistics for selected data:')
    st.write(filtered_df.describe())

    # Data Table
    st.header('Data Table')
    st.write('Displaying selected data in a table:')
    st.dataframe(filtered_df)
