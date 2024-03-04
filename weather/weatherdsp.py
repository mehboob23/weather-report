import pandas as pd

# Load the data
data = pd.read_csv('DSP 2\weather.csv')

print("\n\n Q1: Find all the unique 'Wind Speed' values \n")
unique_wind_speeds = data['Wind Speed_km/h'].unique()
print("Unique Wind Speed values:", unique_wind_speeds)

print("\n\n Q2: Find the number of times when the 'Weather is exactly Clear' \n")
clear_weather_count = data[data['Weather']=='Clear'].shape[0]
print("Number of times when the Weather is exactly Clear:", clear_weather_count)

print("\n\n Q3: Find the number of times when the 'Wind Speed was exactly 4 km/h' \n")
wind_speed_4_count = data[data['Wind Speed_km/h'] == 4].shape[0]
print("Number of times when the Wind Speed was exactly 4 km/h:", wind_speed_4_count)

print("\n\n Q4: Find out all the Null Values in the data \n")
null_values = data.isnull().sum()
print("Null Values in the data:")
print(null_values)

print("\n\n Q5: Rename the column name 'Weather' to 'Weather Condition'\n")
data.rename(columns={'Weather': 'Weather Condition'}, inplace=True)

print("\n\n Q6: What is the mean 'Visibility'? \n")
mean_visibility = data['Visibility_km'].mean()
print("Mean Visibility:", mean_visibility)

print("\n\n Q7: What is the Standard Deviation of 'Pressure' in this data?\n ")
pressure_std_dev = data['Press_kPa'].std()
print("Standard Deviation of Pressure:", pressure_std_dev)

print("\n\n Q8: What is the Variance of 'Relative Humidity' in this data? \n")
humidity_variance = data['Rel Hum_%'].var()
print("Variance of Relative Humidity:", humidity_variance)

print("\n\n Q9: Find all instances when 'Snow' was recorded. \n")
snow_instances = data[data['Weather Condition'] == 'Snow']
print("Instances when Snow was recorded:")
print(snow_instances)

print("\n\n Q10: Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'. \n ")
wind_speed_visibility_instances = data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]
print("Instances when Wind Speed is above 24 and Visibility is 25:")
print(wind_speed_visibility_instances)

print("\n\n Q11: What is the Mean value of each column against each 'Weather Condition'? \n")
mean_values_weather_condition = data.groupby('Weather Condition').mean()
print("Mean value of each column against each Weather Condition:")
print(mean_values_weather_condition)

print("\n\n Q12: What is the Minimum & Maximum value of each column against each 'Weather Condition'? \n")
min_max_values_weather_condition = data.groupby('Weather Condition').agg(['min', 'max'])
print("Minimum & Maximum value of each column against each Weather Condition:")
print(min_max_values_weather_condition)

print("\n\n Q13: Show all the Records where Weather Condition is Fog?\n ")
fog_records = data[data['Weather Condition'] == 'Fog']
print("Records where Weather Condition is Fog:")
print(fog_records)

print("\n\n Q14: Find all instances when 'Weather is Clear' or 'Visibility is above 40'\n ")
clear_visibility_instances = data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]
print("Instances when Weather is Clear or Visibility is above 40:")
print(clear_visibility_instances)

print("\n\n Q15: Find all instances when: A. 'Weather is Clear' and 'Relative Humidity is greater than 50' or B. 'Visibility is above 40'\n")
condition_15 = data[((data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50)) | (data['Visibility_km'] > 40)]
print("Instances when Weather is Clear and Relative Humidity is greater than 50 or Visibility is above 40:")
print(condition_15)
