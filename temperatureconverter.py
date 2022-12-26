def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9/5 + 32
    return fahrenheit


input_temp = float(input("Enter temperature in Celsius: "))
converted_temp = celsius_to_fahrenheit(input_temp)
print(f"Temperature in Fahrenheit: {converted_temp:.2f}")
