import tkinter as tk
import requests
import time

def getWeather(event=None):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"
    
    json_data = requests.get(api).json()

    if json_data.get("cod") != 200:
        location_label.config(text="City not found!", fg="red")
        label1.config(text="")
        label2.config(text="")
        return

    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    
    location_label.config(text=f"Weather in {city.title()}", fg="black")  # 🆕 Location label update
    label1.config(text=final_info)
    label2.config(text=final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

entry_label = tk.Label(canvas, text="Enter Location Name:", font=("poppins", 18))
entry_label.pack(pady=(20, 0))

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=10)
textField.focus()
textField.bind('<Return>', getWeather)

# 🆕 Label to show city after fetching
location_label = tk.Label(canvas, font=("poppins", 20, "bold"))
location_label.pack(pady=5)

label1 = tk.Label(canvas, font=t)
label1.pack()

label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()
