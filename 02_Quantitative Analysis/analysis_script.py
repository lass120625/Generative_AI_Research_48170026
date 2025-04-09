# This is a sample Python script for analyzing survey data
import pandas as pd
data = pd.read_csv('survey_data.csv')
print(data.describe())