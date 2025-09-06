import random

def weather(city):
    conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy", "Windy"]
    temp = random.randint(-5, 40)
    humidity = random.randint(20, 90)
    condition = random.choice(conditions)

    print(f"\nCity: {city}")
    print(f"Temperature: {temp}")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {condition}")


city = input("Enter the name of city: ")
weather(city)
