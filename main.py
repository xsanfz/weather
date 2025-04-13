import requests


def fetch_weather(city):
    response = requests.get(
        f"https://wttr.in/{city}",
        params={'M': '', 'T': '', 'n': '', 'Q': '', 'lang': 'ru'},
        timeout=5
    )
    response.raise_for_status()
    return response.text


def main():
    cities = ["Лондон", "Шереметьево", "Череповец"]

    for city in cities:
        try:
            forecast = fetch_weather(city).strip()
            print(f"{city}: {forecast}")
        except requests.exceptions.HTTPError:
            print(f"Ошибка: не удалось получить прогноз для {city} (HTTP ошибка)")
        except requests.exceptions.ConnectionError:
            print(f"Ошибка соединения при запросе погоды в {city}")
        except requests.exceptions.Timeout:
            print(f"Превышено время ожидания ответа для {city}")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе погоды в {city}: {str(e)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Критическая ошибка: {str(e)}")
