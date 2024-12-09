from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

client = MongoClient('mongodb://localhost:27017/')
db = client['form_templates_db']
templates_collection = db['templates']

def load_templates():
    return list(templates_collection.find())

def create_templates_if_empty():
    if templates_collection.count_documents({}) == 0:
        templates_collection.insert_many([
            {
                "name": "MyForm",
                "email": "email",
                "phone": "phone"
            },
            {
                "name": "OrderForm",
                "order_date": "date",
                "email": "email"
            }
        ])
        print("Шаблоны добавлены в коллекцию.")
    else:
        print("Коллекция уже содержит шаблоны.")

def add_template(template):
    try:
        templates_collection.insert_one(template)
        print(f"Шаблон '{template['name']}' успешно добавлен.")
    except DuplicateKeyError:
        print(f"Шаблон с именем '{template['name']}' уже существует.")

create_templates_if_empty()
