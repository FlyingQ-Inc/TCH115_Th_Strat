import time
from tkinter import *
from tkinter import messagebox as mb
import requests
from plyer import notification

def getNotification():
    cityName = place.get()
    baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
    
    try:
        # Construct the API request URL
        url = baseUrl + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + cityName  
        response = requests.get(url)
        
        # Parse the JSON response
        x = response.json()
        
        # Check if the city is found
        if x.get('cod') != 200:
            mb.showerror("Error", f"City '{cityName}' not found!")
            return
        
        # Extract weather data
        y = x["main"]
        temp = y["temp"] - 273.15  # Convert Kelvin to Celsius
        pres = y["pressure"]
        hum = y["humidity"]
        z = x["weather"]
        weather_desc = z[0]["description"]
        
        # Format the information
        info = (
            f"Here is the weather description for {cityName}:\n"
            f"Temperature = {temp:.2f}°C\n"
            f"Atmospheric pressure = {pres} hPa\n"
            f"Humidity = {hum}%\n"
            f"Weather description = {weather_desc}"
        )
        
        # Send the notification
        notification.notify(
            title="YOUR WEATHER REPORT",
            message=info,
            timeout=5
        )
        time.sleep(7)
    
    except Exception as e:
        mb.showerror('Error', str(e))

# Set up the GUI
wn = Tk()
wn.title("PythonGeeks Weather Desktop Notifier")
wn.geometry('700x200')
wn.config(bg='azure')

Label(wn, text="PythonGeeks Weather Desktop Notifier", font=('Courier', 15), fg='grey19', bg='azure').place(x=100, y=15)
Label(wn, text='Enter the Location:', font=("Courier", 13), bg='azure').place(relx=0.05, rely=0.3)

place = StringVar(wn)
place_entry = Entry(wn, width=50, textvariable=place)
place_entry.place(relx=0.5, rely=0.3)

btn = Button(wn, text='Get Notification', font=7, fg='grey19', command=getNotification)
btn.place(relx=0.4, rely=0.75)

wn.mainloop()
