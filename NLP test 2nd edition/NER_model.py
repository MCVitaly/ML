from transformers import pipeline

# Загружаем предобученную модель для NER
nlp_ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english", aggregation_strategy="simple")

def extract_product_names(text):
    # Передаем текст в модель NER для извлечения названий продуктов
    ner_results = nlp_ner(text)
    # Извлекаем названия продуктов (entity = 'MISC' или другие)
    products = [entity['word'] for entity in ner_results if entity['entity_group'] == 'MISC']
    return products
