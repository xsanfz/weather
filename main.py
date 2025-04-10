import requests


def fetch_weather_data(city):
    try:
        response = requests.get(
            f"https://wttr.in/{city}",
            params={'M': '', 'T': '', 'n': '', 'Q': '', 'lang': 'ru'},
            timeout=5
        )
        response.raise_for_status()
        return f"{city}: {response.text.strip()}"

    except requests.exceptions.HTTPError:
        return f"Ошибка: не удалось получить данные для {city} (HTTP ошибка)"
    except requests.exceptions.ConnectionError:
        return f"Ошибка соединения при запросе погоды для {city}"
    except requests.exceptions.Timeout:
        return f"Превышено время ожидания ответа для {city}"
    except requests.exceptions.RequestException as e:
        return f"Ошибка при запросе погоды для {city}: {str(e)}"


def main():
    cities = ["Лондон", "Шереметьево", "Череповец"]
    for city in cities:
        print(fetch_weather_data(city))


if __name__ == "__main__":
    main()
