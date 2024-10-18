from data_gathering import scrape_page
from NER_model import extract_product_names
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/extract', methods=['POST'])
def extract_products():
    data = request.json
    url = data.get('url')

    # Скрапинг страницы
    page_content = scrape_page(url)
    if page_content is None:
        return jsonify({'error': 'Не удалось получить содержимое страницы'}), 400

    # Извлечение названий продуктов
    product_names = extract_product_names(page_content)

    # Возвращаем результат в формате JSON
    return jsonify({'products': product_names})


if __name__ == "__main__":
    app.run(debug=True)
