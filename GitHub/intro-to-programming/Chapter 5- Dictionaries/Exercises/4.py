rivers = {
    'Yangtze River': 'China',
    'Mississippi River': 'United States',
    'Nile River': 'Egypt',
    'Ganges River': 'India',
    'Rhine River': 'Switzerland',
    }

for river, country in rivers.items():
    print(f"The {river} flows through {country}.")

print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(f"- {river}")

print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(f"- {country}")