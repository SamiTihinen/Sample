print("Calculate fuel consumption.")
Feed = input("Enter travel distance(kilometers): ")
Distance = int(Feed)
Feed = input("Enter fuel usage(liters): ")
FuelUsage = int(Feed)
Consumption = (FuelUsage / Distance) * 100
print(f"Fuel consumption is {Consumption:.2f} l per 100 km")