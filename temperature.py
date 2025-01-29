#use map to convert a list of temperature from celcius to fahrenheit
Celcius_temperature=[98,99,100,102,36,34,35,34,45]
Fahrenheit_temperature=list(map(lambda x:(x*9/5)+32,Celcius_temperature))
print(Fahrenheit_temperature)