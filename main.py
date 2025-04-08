import requests


def fetch_weather_data(city):
    base_url = "https://wttr.in/{}"

    params = {
        'M': '',
        'T': '',
        'n': '',
        'Q': '',
        'lang': 'ru'
    }

    response = requests.get(base_url.format(city), params=params, timeout=5)
    response.raise_for_status()
    return response.text.strip()


def format_weather_message(city, weather_data):
    return f"{city}: {weather_data}"


def process_city(city):
    weather_data = fetch_weather_data(city)
    return format_weather_message(city, weather_data)


def main():
    cities = ["Лондон", "Шереметьево", "Череповец"]

    for city in cities:
        try:
            message = process_city(city)
            print(message)
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при обработке города {city}: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка для города {city}: {e}")


if __name__ == "__main__":
    main()
