"""
Script to plot focus maps for all CSV files in a directory
Author: Maxime
Date: 2023-10-10
Version: 1.0

Description:
This script generates interactive focus maps for all CSV files in a specified directory.
"""

# Standard modules
import os

# Third-party modules
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio


def plot_focus_map(csv_path):
    """
    Generates an interactive focus map from a CSV file.

    Args:
        csv_path (str): Path to the CSV file containing detection results.
    """
    # Load the CSV file
    df = pd.read_csv(csv_path)

    # Calculate the center position and number of occurrences
    df['x'] = (df['xmin'] + df['xmax']) / 2
    df['y'] = (df['ymin'] + df['ymax']) / 2

    # Group by object name and calculate mean position and count
    grouped = df.groupby('name').agg({'x': 'mean', 'y': 'mean', 'name': 'count'}).rename(columns={'name': 'count'}).reset_index()

    # Calculate the center of the graph
    x_center, y_center = grouped['x'].mean(), grouped['y'].mean()

    # Calculate the distance to the center
    grouped['distance'] = np.sqrt((grouped['x'] - x_center)**2 + (grouped['y'] - y_center)**2)

    # Normalize distances for color mapping
    grouped['distance_norm'] = (grouped['distance'] - grouped['distance'].min()) / (grouped['distance'].max() - grouped['distance'].min())

    # Create the interactive plot
    fig = px.scatter(
        grouped, 
        x="x", y="y", 
        size="count",  # Circle size based on occurrence count
        color=1 - grouped["distance_norm"],  # Closer to center = redder
        color_continuous_scale="RdBu_r",  # Inverted color scale (red = close, blue = far)
        hover_name="name",  # Display name on hover
        title=f"Object Distribution with Color Based on Distance from Center: {os.path.basename(csv_path)}"
    )

    # Add black borders to circles
    fig.update_traces(marker=dict(line=dict(width=1, color='black')))

    # Update layout
    fig.update_layout(
        xaxis_title="X",
        yaxis_title="Y",
        coloraxis_colorbar=dict(title="Proximity to Center"),
        template="plotly_white"  # White background for better visibility
    )

    # Open the plot in the browser
    pio.renderers.default = "browser"
    fig.show()


def process_all_csv_files(input_dir):
    """
    Processes all CSV files in the input directory and generates focus maps.

    Args:
        input_dir (str): Directory containing CSV files.
    """
    # Iterate through all files in the input directory
    for filename in os.listdir(input_dir):
        # Check if the file is a CSV
        if filename.lower().endswith('.csv'):
            csv_path = os.path.join(input_dir, filename)
            print(f"Processing CSV file: {filename}")
            plot_focus_map(csv_path)
        else:
            print(f"Skipping unsupported file: {filename}")


def main():
    """
    Main function of the script.
    """
    input_dir = "results_yolo5s"  # Directory containing CSV files
    process_all_csv_files(input_dir)


if __name__ == "__main__":
    main()