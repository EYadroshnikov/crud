import utils.json_service as json_service


# Полный список
def shop_get_all():
    db = json_service.get_database()
    return db["shops"]


# Получить id магазина по названию
def shop_get_one_by_name(name):
    db = json_service.get_database()  # Чтение базы данных
    for elem in db["shops"]:
        if elem["name"] == name:
            return elem['id']
    return {"message": f"Элемент с {name} не найден"}


# Нанять сотрудника
def shop_create_one(shop):
    db = json_service.get_database()  # Чтение базы данных
    last_sellers_id = shop_get_all()[-1]["id"]
    db["shops"].append({"id": last_sellers_id + 1, **shop})
    json_service.set_database(db)  # Перезапись базы данных


def shops_delete_one_by_id(id):
    db = json_service.get_database()  # Чтение базы данных
    for i, elem in enumerate(db["shops"]):
        if elem["id"] == id:
            candidate = db["shops"].pop(i)
            json_service.set_database(db)
            flag = elem["place_id"]
            for i, elem in enumerate(db["place"]):
                if elem['shop_id'] == flag:
                    elem['shop_id'] = None
                    elem['status'] = False
                    json_service.set_database(db)
            for i, elem in enumerate(db["sellers"]):
                if elem['shop_id'] == flag:
                    elem['shop_id'] = None
                    json_service.set_database(db)
            return candidate
    return {"message": f"Элемент с {id} не найден"}
