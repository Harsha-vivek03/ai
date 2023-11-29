 def celsius_to_fahrenheit(celsius_temperature):
    # Formula to convert Celsius to Fahrenheit: F = (C * 9/5) + 32
    fahrenheit_temperature = (celsius_temperature * 9/5) + 32
    return fahrenheit_temperature

def is_below_freezing(fahrenheit_temperature):
    # Check if the temperature in Fahrenheit is below freezing (32°F or 0°C)
    return fahrenheit_temperature < 32

# Test the functions
celsius_temperature = float(input("Enter a temperature in Celsius: "))
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)

print(f"{celsius_temperature}°C is equivalent to {fahrenheit_temperature}°F.")

if is_below_freezing(fahrenheit_temperature):
    print("The temperature is below freezing (32°F or 0°C).")
else:
    print("The temperature is not below freezing.")

	

