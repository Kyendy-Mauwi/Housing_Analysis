import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset from the specified path
df = pd.read_csv("Data/Housing_Production.csv")

# Display the title of the app
st.title("Interactive Housing Data Analysis")

# Show the dataset
st.subheader("Dataset")
st.write(df.head(20))  # Show the first few rows of the DataFrame

# Sidebar for filtering data (optional)
st.sidebar.title("Filter Data")
zoning_filter = st.sidebar.multiselect(
    'Select Zoning Districts',
    options=df['Zoning District'].unique(),
    default=df['Zoning District'].unique()
)

# Filter the DataFrame based on selected Zoning Districts
filtered_df = df[df['Zoning District'].isin(zoning_filter)]

# Show the filtered data
st.write("Filtered Data:", filtered_df)

# Sidebar for selecting two relevant attributes
st.sidebar.subheader("Select Attributes for Comparison")
column_1 = st.sidebar.selectbox('Select the first attribute', options=filtered_df.select_dtypes(include=['number']).columns)
column_2 = st.sidebar.selectbox('Select the second attribute', options=filtered_df.select_dtypes(include=['number']).columns)

# Option for showing a scatter plot of the two attributes
st.subheader(f"Scatter Plot of {column_1} vs {column_2}")
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=filtered_df, x=column_1, y=column_2, ax=ax)
ax.set_title(f"Scatter Plot of {column_1} vs {column_2}")
st.pyplot(fig)  # Pass the figure to st.pyplot()

# Option for showing the correlation matrix
st.subheader("Correlation Matrix")
if st.checkbox('Show Correlation Matrix'):
    # Select only numeric columns
    numeric_data = filtered_df.select_dtypes(include=['number'])

    # Compute the correlation matrix
    correlation_matrix = numeric_data.corr()

    # Plot the heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', ax=ax)

    # Display the plot
    st.pyplot(fig)  # Pass the figure to st.pyplot()

# Option for showing histograms
st.subheader("Histograms")
column_for_histogram = st.selectbox(
    'Select a column for the histogram',
    options=filtered_df.select_dtypes(include=['number']).columns
)

# Plot the selected column histogram
fig, ax = plt.subplots(figsize=(10, 6))
filtered_df[column_for_histogram].hist(bins=20, ax=ax)
ax.set_title(f"Histogram of {column_for_histogram}")
st.pyplot(fig)  # Pass the figure to st.pyplot()

# Option for showing a boxplot comparison
st.subheader("Boxplot Comparison")
column_for_boxplot = st.selectbox(
    'Select a column for the boxplot',
    options=filtered_df.select_dtypes(include=['number']).columns
)

# Show boxplot
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_df, x='Zoning District', y=column_for_boxplot, ax=ax)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)  # Rotate the x-axis labels for better readability
ax.set_title(f"Boxplot of {column_for_boxplot} by Zoning District")
st.pyplot(fig)  # Pass the figure to st.pyplot()
