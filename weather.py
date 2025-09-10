import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=fa"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        print(f"🌡️ دما در {city}: {temp}°C")
        print(f"🌥️ وضعیت: {desc}")
    else:
        print("❌ شهر پیدا نشد یا API اشتباهه.")

if __name__ == "__main__":
    print("🌦️ AhmadWeather - وضعیت آب‌وهوا احمد جان 😤")
    city = input("🧭 نام شهر رو وارد کن: ")
    api_key = input("🔑 کلید API رو وارد کن: ")
    get_weather(city, api_key)
