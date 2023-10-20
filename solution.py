from collections import Counter
from functools import reduce

# Given data
temperatures_in_celsius = [20.5, 22.4, 19.8, 21.3, 18.9]
air_quality_index = [45, 62, 150, 55, 112]  # Values > 100 are considered "poor" air quality.
pollutants = ["CO2", "Ozone", "CO2", "SO2", "CO2"]
humidity_levels = [45, 15, 60, 48, 53]

# 1. Temperature Conversion:
temperatures_in_fahrenheit = list(map(lambda c: (c * 9/5) + 32, temperatures_in_celsius))

# 2. Poor Air Quality Identification:
poor_air_quality = list(filter(lambda x: x > 100, air_quality_index))

# 3. Most Common Pollutant:
common_pollutant = Counter(pollutants).most_common(1)[0][0]

# 4. Average Humidity Calculation:
total_humidity = reduce(lambda x, y: x + y, humidity_levels)
average_humidity = total_humidity / len(humidity_levels)

# Bonus:
poor_air_quality_locations = [(i, temp, common_pollutant) for i, (temp, aqi) in enumerate(zip(temperatures_in_fahrenheit, air_quality_index)) if aqi > 100]

# Printing the results
print("Temperatures in Fahrenheit:", temperatures_in_fahrenheit)
print("Locations with Poor Air Quality:", poor_air_quality)
print("Most Common Pollutant:", common_pollutant)
print("Average Humidity:", average_humidity)

print("\nBonus:")
for loc, temp, pollutant in poor_air_quality_locations:
    print(f"Location {loc} with temperature {temp}F has poor air quality and the most common pollutant in all locations is {pollutant}.")
