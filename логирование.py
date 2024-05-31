import requests
from requests.exceptions import RequestException

# Список URL-адресов для проверки
urls = [
    "https://www.youtube.com/",
    "https://wikipedia.org",
    "https://yahoo.com",
    "https://yandex.ru",
    "https://whatsapp.com",
    "https://amazon.com",
    "https://www.ozon.ru",
    "https://instagram.com",
    "https://twitter.com"
]

# Функция для отправки GET-запроса и записи результата в соответствующий файл лога
def log_response(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open("success_responses.log", "a") as file:
                file.write(f"INFO: '{url}', response - {response.status_code}\n")
        else:
            with open("bad_responses.log", "a") as file:
                file.write(f"WARNING: '{url}', response - {response.status_code}\n")
    except RequestException as e:
        with open("blocked_responses.log", "a") as file:
            file.write(f"ERROR: {url}, {str(e)}\n")

# Проверка каждого URL и запись результатов в логи
for url in urls:
    log_response(url)