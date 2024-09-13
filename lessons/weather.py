def get_weather_report() -> str:
    """Takes a weather related input and gives feedback."""
    weather: str = input("What is the weather? ")  # weather input
    if weather == "rainy" or weather == "cold":  # string boolean
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather.")
    return weather  # return the original input


print(get_weather_report())
