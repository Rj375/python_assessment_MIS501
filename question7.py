temperature = float(input("Enter the temperature value: "))
conversionForm = int(input("Enter the conversion form (1 for Centigrade to Fahrenheit, 2 for Fahrenheit to Centigrade): "))

# it converts the temperature
if conversionForm == 1:
    # From Centigrade to Fahrenheit
    temperatureConverted = (9/5) * temperature + 32
    print(temperature, "Centigrade =", temperatureConverted, "Fahrenheit")
elif conversionForm == 2:
    # From Fahrenheit to Centigrade
    temperatureConverted = (5/9) * (temperature - 32)
    print(temperature, "Fahrenheit =", temperatureConverted, "Centigrade")
else:
    print("Invalid entry.")