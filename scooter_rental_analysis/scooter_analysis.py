# scooter_analysis.py
# Author: Logan Kaliba
# Project: Scooter Rental Data Analysis
# Description: Explore, visualize, and model scooter rental data using Python and linear regression.

# ------------------------------------------------------------------------------
# 1. Import Libraries
# ------------------------------------------------------------------------------
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

# ------------------------------------------------------------------------------
# 2. Load Data
# ------------------------------------------------------------------------------
scooter_data = pd.read_csv('https://bit.ly/scooter-rentals')

# ------------------------------------------------------------------------------
# 3. Initial Exploration
# ------------------------------------------------------------------------------
# Number of records
scooter_data.shape  # Expected: (731 records, 14 columns)

# Question 2: Data types
scooter_data.info()

# ------------------------------------------------------------------------------
# 4. Rename Columns
# ------------------------------------------------------------------------------
scooter_data = scooter_data.rename(columns={
    'yr': 'year',
    'mnth': 'month',
    'hum': 'humidity_norm',
    'temp': 'temp_norm',
    'atemp': 'temp_felt_norm',
    'wind': 'wind_norm',
    'registered': 'rentals_registered',
    'unregistered': 'rentals_unregistered'
})

# Preview renamed columns
scooter_data.head()

# ------------------------------------------------------------------------------
# 5. Replace Season Codes with Names
# ------------------------------------------------------------------------------
scooter_data['season'] = scooter_data['season'].replace(
    [1, 2, 3, 4], ['winter', 'spring', 'summer', 'fall']
)
scooter_data.head()

# ------------------------------------------------------------------------------
# 6. Feature Engineering
# ------------------------------------------------------------------------------
scooter_data['rentals_total'] = (
    scooter_data['rentals_registered'] + scooter_data['rentals_unregistered']
)
scooter_data.head()

# Descriptive statistics
scooter_data.describe()

# ------------------------------------------------------------------------------
# 7. Check for Missing Values and Duplicates
# ------------------------------------------------------------------------------
scooter_data.isnull().sum()
sum(scooter_data.duplicated(scooter_data.columns))

# ------------------------------------------------------------------------------
# 8. Visualizations and Correlation Analysis
# ------------------------------------------------------------------------------
# Distribution of total rentals
sns.displot(scooter_data['rentals_total'])

# Scatterplot: unregistered vs registered by workday
sns.scatterplot(data=scooter_data, x='rentals_unregistered', y='rentals_registered', hue='workday')

# Swarmplot: rentals by season
sns.catplot(data=scooter_data, x='season', y='rentals_total', kind='swarm')

# Lineplot: rentals by month/year
sns.relplot(data=scooter_data, x='month', y='rentals_total', hue='year', kind='line')

# KDE Pairplot: weather vs rentals
sns.pairplot(scooter_data, vars=['temp_norm', 'temp_felt_norm', 'humidity_norm', 'wind_norm', 'rentals_total'], kind='kde')

# Correlation Heatmap
scooter_data_dp = scooter_data.drop(columns=[
    'ID', 'date', 'year', 'month', 'weekday', 'workday', 'season',
    'holiday', 'wind_norm', 'rentals_registered', 'rentals_unregistered'
])
sns.heatmap(scooter_data_dp.corr(), annot=True)

# Correlation between "rentals_total" and "temp_norm" ≈ 0.63
scooter_data_dp.corr()

# ------------------------------------------------------------------------------
# 9. Prepare for Modeling
# ------------------------------------------------------------------------------
# Define features and target
X = scooter_data[['temp_norm']]
y = scooter_data['rentals_total']

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# Fit linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# ------------------------------------------------------------------------------
# 10. Model Evaluation
# ------------------------------------------------------------------------------
# Intercept
print(model.intercept_)

# Coefficient for temp_norm
print(model.coef_)

# Prediction for temp_norm = 0.30
new_X = [[0.30]]
print(model.predict(new_X))

# Predict on test data
y_pred = model.predict(X_test.values)

# R-squared score
metrics.r2_score(y_test, y_pred)  # Expected ≈ 0.37 (moderate model performance)
