import json


# Чтение базы данных
def get_database():
    with open("db.json", encoding="utf-8") as db_file:
        return json.load(db_file)


# Перезапись базы данных
def set_database(db):
    with open("db.json", "w", encoding="utf-8", ) as db_file:
        json.dump(db, db_file, indent=3)
