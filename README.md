# Investment Growth Comparison: QCOM vs. AMD (2022)

This Python script provides a comparative analysis of the investment performance for **Qualcomm (QCOM)** and **Advanced Micro Devices (AMD)** throughout the fiscal year 2022. By processing historical CSV data, the tool calculates and visualizes the cumulative returns of both stocks, allowing users to see how a theoretical $1 investment would have fluctuated over the course of the year.

## Features

* **Dynamic Data Loading**: Flexible input system that allows users to specify their own local CSV filenames for both stock datasets.

* **Automated Data Cleaning**: Robust handling of financial string formats, specifically stripping currency symbols (e.g., "$") and converting them into numeric floats for calculation.

* **Time-Series Filtering**: Automatically isolates data from the year 2022 to ensure a head-to-head comparison over the same economic period.

* **Cumulative Return Tracking**: Calculates the daily percentage change and the resulting cumulative product to track investment growth over time.

* **High-Resolution Visualization**: Generates a professional-grade line chart using Matplotlib, featuring custom scaling, grid lines, and clear labeling for easy interpretation.

## Built With

* **Python 3**: The core programming language.

* **Pandas**: Used for sophisticated data manipulation, merging dataframes, and time-series analysis.

* **Matplotlib**: Utilized for rendering the final graphical representation of the investment trends.

## Key Achievement in Code

The standout technical achievement in this script is the **seamless data synchronization through relational merging**. By using:

```
Python
Comparison_table = pd.merge(QCOM, AMD, on='Date', suffixes=('_QCOM', '_AMD'))
```

The code effectively handles potential gaps in trading days between two separate datasets. By performing an inner join on the Date column, it ensures that the resulting visualization is perfectly aligned, comparing the two stocks only on days where data exists for both. This prevents "ghost" data points and ensures the mathematical accuracy of the comparison plot.
