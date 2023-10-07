import tkinter as tk
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from PIL import ImageGrab
import os
import time


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use("xpnative")

        self.create_gui()

    def create_gui(self):
        self.frame = ttk.Frame(self.root, padding=20)
        self.frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        self.city_label = ttk.Label(self.frame, text="Enter City:")
        self.city_label.grid(column=0, row=0, sticky=tk.W)

        self.city_entry = ttk.Entry(self.frame)
        self.city_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

        self.get_weather_button = ttk.Button(self.frame, text="Get Weather", command=self.get_weather)
        self.get_weather_button.grid(column=2, row=0, sticky=tk.E)

        self.weather_label = ttk.Label(self.frame, text="")
        self.weather_label.grid(column=0, row=1, columnspan=3)

        self.screenshot_button = ttk.Button(self.frame, text="Take Screenshot", command=self.take_screenshot)
        self.screenshot_button.grid(column=0, row=2, columnspan=3)

        self.screenshot_window = None

    def get_weather(self):
        city = self.city_entry.get()
        if city:
            url = f"https://www.google.com/search?q=погода+в+{city}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                weather_block = soup.find('div', class_='BNeawe iBp4i AP7Wnd')

                if weather_block:
                    weather_text = weather_block.text.strip()
                    self.weather_label.config(text=f"Weather in {city}: {weather_text}")
                else:
                    self.weather_label.config(text=f"Weather data not found for {city}")
            else:
                self.weather_label.config(text="Failed to fetch weather data")
        else:
            self.weather_label.config(text="Please enter a city")

    def take_screenshot(self):
        if self.screenshot_window:
            self.screenshot_window.destroy()

        root.withdraw()
        im = ImageGrab.grab()
        root.deiconify()

        downloads_folder = os.path.expanduser("~\\Downloads")

        screenshot_path = os.path.join(downloads_folder, "weather_screenshot.png")
        im.save(screenshot_path)

        self.screenshot_window = tk.Toplevel()
        self.screenshot_window.title("Screenshot")
        screenshot_label = tk.Label(self.screenshot_window, text=f"Screenshot saved to {screenshot_path}")
        screenshot_label.pack(padx=20, pady=20)

        self.screenshot_window.after(1000, self.close_screenshot_window)

    def close_screenshot_window(self):
        if self.screenshot_window:
            self.screenshot_window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()