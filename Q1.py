#python program to convert celcius to feranheit and vice-versa
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

fahrenheit = float(input("Enter temperature in fahrenheit:"))
celcius =  fahrenheit-32*5/9
print(f"{fahrenheit}°F is equal to {celcius:.2f} °C ")

print(f"{fahrenheit}°F is equal to {celcius:.2f} °C ")
