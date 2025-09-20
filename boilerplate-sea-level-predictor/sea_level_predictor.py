import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')
    
    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit (all data)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2050))
    line1 = slope * years_extended + intercept
    plt.plot(years_extended, line1, 'r', label='Best Fit (1880-2050)')

    # Create second line of best fit (from 2000)
    recent_df = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2050))
    line2 = slope2 * years_recent + intercept2
    plt.plot(years_recent, line2, 'g', label='Best Fit (2000-2050)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save plot and return data for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
