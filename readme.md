# GeoInsight: India District Data Explorer - Streamlit App

This Streamlit application, named "India Data Explorer," is designed to help you visualize and explore data related to various states in India. It provides an interactive interface to select states, primary parameters, and secondary parameters, and then displays the corresponding data on a scatter map and in tables.

## Features

### 1. Sidebar Controls

- **Select States**: You can choose one or more Indian states from the sidebar dropdown menu. The data will be filtered based on your selection.

- **Select a Primary Parameter**: This dropdown allows you to select the primary parameter that will be presented as the size of data points on the map.

- **Select a Secondary Parameter**: This dropdown allows you to select the secondary parameter to be displayed as the color of data points on the map.

- **Plot Graph Button**: Clicking this button will generate and display a scatter map with data points that reflect the chosen parameters and states.

### 2. Scatter Map Visualization

- **Size and Color Representation**: The size of the data points on the map represents the primary parameter, while the color represents the secondary parameter. 

- Overall India Data: If you select "Overall India" in the state dropdown, the application will display data for the entire country.

### 3. Data Summary

- **Data Summary**: This section gives summary statistics for the selected data, allowing you to see how the values are distributed.

### 4. Data Table

- **Data Table**: You can view the selected data in a tabular style here, making it easy to investigate individual data points.

## How to Use

1. Clone the repository and make sure you have the necessary libraries installed, including Streamlit, NumPy, pandas, and Plotly Express.

2. Place your data file (in this case, 'india.csv') in the same directory as the script.

3. Run the Streamlit app by executing the following command in your terminal:

   ```
   streamlit run your_script_name.py
   ```

4. Use the sidebar controls to select states, primary and secondary parameters, and click the "Plot Graph" button to generate visualizations and data summaries.

## Note

- This application assumes you have a CSV file named "india.csv" that contains the information you want to explore. Make sure the data file's structure matches the code's expectations.

- You can customize the code further to adapt it to your specific dataset or visualization preferences.

Enjoy exploring and visualizing data related to various states in India with this Streamlit app!