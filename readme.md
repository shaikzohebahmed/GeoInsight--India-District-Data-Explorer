# GeoInsight: India District Data Explorer - Streamlit App

Welcome to **GeoInsight: India District Data Explorer**, a Streamlit application designed to help you visualize and explore data related to various states in India. This interactive app provides a user-friendly interface to select states, primary parameters, and secondary parameters, and then displays the corresponding data on a scatter map and in tables.

## Features

### 1. Sidebar Controls

- **Select States**: Choose one or more Indian states from the sidebar dropdown menu to filter the data based on your selection.

- **Select a Primary Parameter**: Pick the primary parameter to be displayed as the size of data points on the map.

- **Select a Secondary Parameter**: Choose a secondary parameter to be displayed as the color of data points on the map.

- **Plot Graph Button**: Generate and display a scatter map with data points representing the selected parameters and states.

### 2. Scatter Map Visualization

- **Size and Color Representation**: The size of data points on the map reflects the primary parameter, while the color represents the secondary parameter.

- **Overall India Data**: By selecting "Overall India" in the state dropdown, you can view data for the entire country.

### 3. Data Summary

- **Data Summary**: Obtain summary statistics for the selected data, gaining insights into data distribution.

### 4. Data Table

- **Data Table**: View the selected data in a tabular format, facilitating exploration of individual data points.

## How to Use

1. **Clone the Repository**: Start by cloning the project repository and ensuring you have the necessary libraries installed, including Streamlit, NumPy, pandas, and Plotly Express.

2. **Prepare Your Data**: Place your data file (in this case, 'india.csv') in the same directory as the provided script.

3. **Run the Streamlit App**: Open a terminal or command prompt, navigate to the project directory, and run the Streamlit app with the following command:

   ```bash
   streamlit run your_script_name.py
   ```

   Replace `your_script_name.py` with the name of the Python file containing the code.

4. **Explore Your Data**: Utilize the sidebar controls to select states, primary and secondary parameters, and click the "Plot Graph" button to generate visualizations and data summaries.

## Note

- This application assumes that you have a CSV file named "india.csv" containing the data you wish to explore. Ensure that the data file's structure aligns with the code's expectations.

- Feel free to customize the code further to suit your specific dataset or visualization preferences.

Enjoy exploring and visualizing data related to various states in India with the **GeoInsight: India District Data Explorer** Streamlit app!

## Project URL

For direct access to the app, visit: [GeoInsight: India District Data Explorer](https://geoinsight--india-district-data-explorer.streamlit.app/)