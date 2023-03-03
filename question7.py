
temperature = float(input("Enter the temperature value: "))
conversion_form = int(input("Enter the conversion form (1 for Centigrade to Fahrenheit, 2 for Fahrenheit to Centigrade): "))

# it converts the temperature
if conversion_form == 1:
    # From Centigrade to Fahrenheit
    temperature_converted = (9/5) * temperature + 32
    print(temperature, "Centigrade =", temperature_converted, "Fahrenheit")
elif conversion_form == 2:
    # From Fahrenheit to Centigrade
    temperature_converted = (5/9) * (temperature - 32)
    print(temperature, "Fahrenheit =", temperature_converted, "Centigrade")
else:
    print("Invalid entry.")