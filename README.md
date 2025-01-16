# Housing Production Data Analysis

This repository contains an analysis of housing production data, focusing on various attributes such as zoning districts and production metrics. The dataset can be explored interactively using a **Streamlit** web app that allows users to visualize key relationships in the data and filter it based on relevant attributes.

## Dataset Overview

The **Housing Production** dataset contains information on housing production, including attributes such as:

- **Zoning District**: The zoning designation of the area where the housing units are located.
- **Various housing production metrics**: This includes measures such as the number of units, cost of production, and area of land utilized for different projects.
- **Additional columns**: The dataset includes several numeric and categorical variables that are useful for understanding trends in housing production.

## Streamlit App

This repository includes a **Streamlit** web app that provides an interactive interface to visualize and analyze the housing production data. Users can explore the following features:

### Key Features:
- **Dataset Preview**: View the first few rows of the dataset.
- **Zoning District Filter**: Filter the dataset based on selected zoning districts using a sidebar multi-select widget.
- **Scatter Plot**: Select two numeric attributes to visualize their relationship in a scatter plot.
- **Correlation Matrix**: View a heatmap showing the correlation between numeric attributes in the dataset.
- **Histogram**: Generate histograms for selected numeric attributes to explore their distribution.
- **Boxplot**: Compare numeric attributes across zoning districts using a boxplot.

### How to Use the App:
1. **Dataset Filtering**:
   - On the sidebar, use the **"Zoning District"** filter to select specific zoning districts for analysis.
2. **Attribute Comparison**:
   - Choose two numeric attributes for comparison using the **"Select Attributes for Comparison"** dropdowns. This will generate a scatter plot.
3. **Visualizations**:
   - You can view the correlation matrix, histograms, and boxplots by selecting the corresponding options in the sidebar.

### Prerequisites:
To run the app locally, you need to have Python and Streamlit installed. Follow these steps:

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. **Install Dependencies**:
   Make sure to create and activate a virtual environment, then install the required packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

   Or if you prefer, you can manually install the dependencies:
   ```bash
   pip install streamlit pandas matplotlib seaborn
   ```

## Running the Streamlit App:

1. **Start the App**:
   Navigate to the directory where the app file (`app.py`) is located and run:
   ```bash
   streamlit run app.py
   ```

2. **View the App**:
   After running the above command, Streamlit will open the app in your default web browser.

## Example Usage:

Once the app is running, you can interact with the following widgets:

- **Zoning Districts Filter**: Select which zoning districts to include in the analysis.
- **Attributes for Comparison**: Choose two numeric attributes to display their relationship in a scatter plot.
- **Correlation Matrix**: Show a heatmap of the correlation between numeric attributes.
- **Histogram**: Visualize the distribution of a selected numeric attribute.
- **Boxplot**: View a boxplot comparing a selected numeric attribute by zoning district.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

