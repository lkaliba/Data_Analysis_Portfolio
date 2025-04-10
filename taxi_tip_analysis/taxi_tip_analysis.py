# taxi_tip_analysis.py
# Author: Logan Kaliba
# Date: February 13, 2025
# Project: Inferential Statistics Analysis – Taxi Tip Comparison
# Description: Analyze tip amounts for yellow vs green taxis using a 2-sample t-test.
# Context: Tasked as a data analyst at a taxi company to determine if there's a statistically significant difference in average tips between yellow and green cabs.

# ==============================================================================
# 1. Import Libraries
# ==============================================================================
import pandas as pd
import seaborn as sns
from scipy import stats

# ==============================================================================
# 2. Load and Explore the Dataset
# ==============================================================================

# Load the CSV file into a dataframe.
taxi_samples = pd.read_csv('https://bit.ly/taxi-samples')

# Dimensions of the dataset
taxi_samples.shape

# Column data types
taxi_samples.info()

# Preview first 5 records
taxi_samples.head()

# Descriptive stats for numeric columns
taxi_samples.describe()

# ==============================================================================
# 3. Segment Data by Cab Color and Visualize
# ==============================================================================

# Create separate DataFrames for yellow and green taxis
df_taxi_yellow = taxi_samples[taxi_samples['color'] == 'green']
df_taxi_green = taxi_samples[taxi_samples['color'] == 'yellow']

# Plot distribution of tips for yellow cabs
sns.displot(df_taxi_yellow['tip'])

# Plot distribution of tips for green cabs
sns.displot(df_taxi_green['tip'])

# ==============================================================================
# 4. Test for Normality
# ==============================================================================

# Define tip columns for each group
x = df_taxi_yellow['tip']
y = df_taxi_green['tip']

# Perform normality tests
print(stats.normaltest(x)) # p-value: 0.00009789270985641703
print(stats.normaltest(y)) # p-value: 0.16181672060489052

# ==============================================================================
# 5. Test for Equal Variance (Bartlett’s Test)
# ==============================================================================

# Assume equal variances as p-value 0.379 > 0.05
stats.bartlett(x, y)

# ==============================================================================
# 6. Conduct 2-Sample T-Test
# ==============================================================================

# Conduct the independent t-test
stats.ttest_ind(x, y)

# Interpretation
# Since the p-value 0.963 > 0.05, we fail to reject the null hypothesis.