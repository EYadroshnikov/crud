import utils.json_service as json_service
import components.category as category


# Полный список
def product_get_all():
    db = json_service.get_database()
    return db["product"]


def get_all_in_category(category):
    db = json_service.get_database()
    products = []
    for elem in db['product']:
        if elem['category'] == category:
            products.append(elem['name'])


def product_cnt():
    db = json_service.get_database()
    return len(db["product"])


def add_new_product(product):
    db = json_service.get_database()  # Чтение базы данных
    last_sellers_id = product()[-1]["id"]
    db["sellers"].append({"id": last_sellers_id + 1,
                          **product,
                          "category_id": category.get_id_by_category(product['category'])})
    json_service.set_database(db)


def delete_one_by_id(id):
    db = json_service.get_database()
    for i, elem in enumerate(db['product']):
        if elem['id'] == id:
            candidate = db['product'].pop(i)
            json_service.set_database(db)
            return candidate
    return False
