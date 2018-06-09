from pyowm import OWM


owm = OWM(API_key='c4c27280349fce4e3bb120031151146b')

obs = owm.weather_at_place('Albuquerque, USA')  # Toponym
obs = owm.weather_at_coords(-0.107331,51.503614)

w = obs.get_weather()

print(w.get_clouds())
print(w.get_rain())
print(w.get_temperature("fahrenheit"))

temp_dictionary = w.get_temperature("fahrenheit")
print("The max temperature is ", temp_dictionary['temp_max'])

