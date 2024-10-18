import requests
from bs4 import BeautifulSoup

def scrape_page(url):
    try:
        # Отправляем запрос на сайт
        response = requests.get(url)
        if response.status_code == 200:
            # Парсим HTML-код страницы
            soup = BeautifulSoup(response.content, 'html.parser')
            # Извлекаем текст страницы
            return soup.get_text()
        else:
            return None
    except Exception as e:
        print(f"Ошибка при обработке URL {url}: {str(e)}")
        return None
