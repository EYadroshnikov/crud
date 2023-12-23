import utils.json_service as json_service


# Полный список
def sellers_get_all():
    db = json_service.get_database()
    return db["sellers"]


# Получить id сотрудника по имени
def sellers_get_one_by_name(name):
    db = json_service.get_database()  # Чтение базы данных
    for elem in db["sellers"]:
        if elem["name"] == name:
            return elem['id']
    return {"message": f"Элемент с {name} не найден"}


# Обновить информацию о продавце
def sellers_update_one_by_id(id, seller):
    db = json_service.get_database()
    for i, elem in enumerate(db["sellers"]):
        if elem["id"] == id:
            elem["name"] = seller["name"]
            elem["shop_id"] = seller["shop_id"]
            elem["contacts"] = seller["contacts"]
            json_service.set_database(db)
            return elem
    return {"message": f"Элемент с {id} не найден"}


# Уволнение сотрудника по id
def sellers_delete_one_by_id(id):
    db = json_service.get_database()  # Чтение базы данных
    for i, elem in enumerate(db["sellers"]):
        if elem["id"] == id:
            candidate = db["sellers"].pop(i)
            json_service.set_database(db)  # Перезапись базы данных
            return candidate
    return False


# Нанять сотрудника
def sellers_create_one(seller):
    db = json_service.get_database()  # Чтение базы данных
    last_sellers_id = sellers_get_all()[-1]["id"]
    db["sellers"].append({"id": last_sellers_id + 1, **seller})
    json_service.set_database(db)  # Перезапись базы данных
