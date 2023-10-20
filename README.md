<!-- Exercise: Advanced Environmental Data Analysis -->
# Backstory:

You've recently been promoted to a senior data analyst role at EcoWatch, an environmental protection agency. The organization has now upgraded its data collection efforts, and not only are they collecting air quality and temperature, but they're also collecting humidity levels and the types of pollutants found at different locations.

You need to process and analyze this enhanced dataset using advanced Python techniques.

# Objective:
Use the map function to convert all temperatures from Celsius to Fahrenheit.
Use the filter function to identify locations with poor air quality.
Identify the most common pollutant across locations using the collections module.
Calculate the average humidity using the reduce function.

# Data:

temperatures_in_celsius = [20.5, 22.4, 19.8, 21.3, 18.9]

pollutants = ["CO2", "Ozone", "CO2", "SO2", "CO2"]
air_quality_index = [45, 62, 150, 55, 112]  
#NOTE: Values > 100 are considered "poor" air quality.


humidity_levels = [45, 55, 60, 48, 53]

# Tasks:
1) Temperature Conversion:
- Use the map function to convert each temperature from Celsius to Fahrenheit.
Formula: (celsius * 9/5) + 32
- Store the results in a new list called temperatures_in_fahrenheit.

2) Poor Air Quality Identification:
- Use the filter function to identify values in air_quality_index that exceed 100.
- Store these values in a new list called poor_air_quality.

3) Most Common Pollutant:
- Using the collections.Counter class, determine the most common pollutant in the pollutants list.

4) Average Humidity Calculation:
- Use the reduce function from the functools module to calculate the sum of humidity levels.
- Divide the sum by the number of locations to determine the average humidity.

# Bonus:
Pair up the temperatures_in_fahrenheit, poor_air_quality, and the most common pollutant using the zip function. 
Then, print out locations (index) that have poor air quality alongside their respective temperatures and the most common pollutant. Feel free to get creative in how you choose to display your information
Note: This part requires use of the enumerate function too.
