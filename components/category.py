import utils.json_service as json_service
import components.product as product


# Полный список
def category_get_all():
    db = json_service.get_database()
    return db["category"]


# Получить id категории товаров
def category_get_one_by_name(name):
    db = json_service.get_database()  # Чтение базы данных
    for elem in db["category"]:
        if elem["name"] == name:
            return elem['id']
    return {"message": f"Элемент с {name} не найден"}


# Удалить категорию товаров
def category_delete_one_by_id(id):
    db = json_service.get_database()  # Чтение базы данных
    for i, elem in enumerate(db["category"]):
        if elem["id"] == id:
            candidate = db["category"].pop(i)
            json_service.set_database(db)  # Перезапись базы данных

            for item in db['product']:
                if item['category_id'] == id:
                    product.delete_one_by_id(item['id'])

            return candidate
    return {"message": f"Элемент с {id} не найден"}


# Добавить категорию товаров
def category_create_one(category):
    db = json_service.get_database()  # Чтение базы данных
    last_category_id = category_get_all()[-1]["id"]
    db["category"].append({"id": last_category_id + 1, **category})
    json_service.set_database(db)  # Перезапись базы данных


def get_id_by_category(category):
    db = json_service.get_database()  # Чтение базы данных
    for elem in db["category"]:
        if elem["name"] == category:
            return elem['id']
    return {"message": f"Элемент с {category} не найден"}


def get_category_by_id(id):
    db = json_service.get_database()
    for elem in db['category']:
        if elem['id'] == id:
            return elem['name']
    return {"message": f"Элемент с id {id} не найден"}
