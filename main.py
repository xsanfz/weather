import requests


def get_weather(cities):
    url_template = "https://wttr.in/{}?MTqnQ&lang=ru"

    for city in cities:
        try:
            response = requests.get(url_template.format(city))
            response.raise_for_status()
            print(f"\n{city}")
            print(response.text)
        except requests.exceptions.RequestException as e:
            print(f"\nОшибка при запросе погоды для {city}: {e}")


if __name__ == "__main__":
    CITIES = ["Лондон", "Шереметьево", "Череповец"]
    get_weather(CITIES)


