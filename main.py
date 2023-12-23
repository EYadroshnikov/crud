import components.sellers as seller
import components.category as category
import components.product as product
import components.shops as shop
import utils.menu as menu

while True:
    try:
        print('Разделы: ')
        print('1. Sellers commands')
        print('2. Category commands')
        print('3. Place commands')
        print('4. Shops commands')
        n_commands = int(input('Введите номер раздела команд: '))
        if 0 < n_commands < 5:
            menu.print_commands(n_commands)
            command = int(input('Введите команду: '))
        else:
            print('Такого раздела нет!')

        """
        Sellers commands
        """
        if n_commands == 1:
            # получить id сотрудника по имени
            if command == 1:
                name = str(input('Введите имя сотрудника: '))
                print(f'id сотрудника {name}: ', seller.sellers_get_one_by_name(name))

            # уволить сотрудника
            if command == 2:
                id = int(input('Введите id сотрудника: '))
                if not seller.sellers_delete_one_by_id(id):
                    print('Такого id не существует!')

            # нанять сотрудника
            if command == 3:
                name = str(input('Введите имя нового сотрудника: '))
                shop_id = int(input('id магазина, где работает сотрудник: '))
                email = str(input('Введите email сотрудника: '))
                phone = str(input('Введите телефон сотрудника: '))
                seller.sellers_create_one({
                    "name": f"{name}",
                    "shop_id": f'{shop_id}',
                    "contacts": {
                        "email": f"{email}",
                        "phone": f"{phone}"
                    }})

            # обновить инфу по id
            if command == 4:
                id = int(input('Введите id сотрудника для обновления информации: '))
                if seller.sellers_get_all()[0]["id"] <= id <= seller.sellers_get_all()[-1]["id"]:
                    name = str(input('Введите имя сотрудника: '))
                    shop_id = int(input('id магазина, где работает сотрудник: '))
                    email = str(input('Введите email сотрудника: '))
                    phone = str(input('Введите телефон сотрудника: '))
                    seller.sellers_update_one_by_id(id, {
                        "name": f"{name}",
                        "shop_id": f'{shop_id}',
                        "contacts": {
                            "email": f"{email}",
                            "phone": f"{phone}"
                        }})
                else:
                    print('Такого сотрудника не существует!')

        """""
        Category commands:
        """""
        if n_commands == 2:
            # Category.id
            if command == 1:
                name = str(input('Введите название категории: '))
                print(f'id категории {name}: ', category.category_get_one_by_name(name))

            # Удалить категорию товаров
            if command == 2:
                id = int(input('Введите id категории: '))
                if category.category_get_all()[0]["id"] <= id <= category.category_get_all()[-1]["id"]:
                    category.category_delete_one_by_id(id)
                else:
                    print('Такой категории не существует!')

            # Добавить категорию товаров
            if command == 3:
                name = str(input('Введите новую категорию товаров: '))
                category.category_create_one({
                    "name": f"{name}"
                })

        """""
        product commands:
        """""
        if n_commands == 3:
            if command == 1:
                print(product.product_cnt())

            if command == 2:
                name = str(input('Введите название товара: '))
                category_name = str(input('Введите название категории товаров: '))
                if product.add_new_product({
                    'name': name,
                    'category': category_name
                }):
                    print(f'Товар {name} успешно добавлен')
                else:
                    print('something went wrong...')

            if command == 3:
                category = str(input('введите название категории'))
                for i, name in enumerate(product.get_all_in_category(category)):
                    print(f'{i + 1}. {name}')

        """""
        Shops commands:
        """""
        if n_commands == 4:
            # Shop.id
            if command == 1:
                name = str(input('Введите название магазина: '))
                print(f'id магазина {name}: ', shop.shop_get_one_by_name(name))

            # Shop.add
            if command == 2:
                name = str(input('Введите название нового магазина: '))
                category_id = int(input('id категории товаров: '))
                shop.shop_create_one({
                    "name": f"{name}",
                    "category_id": f'{category_id}',
                })

            # Shop.del
            if command == 3:
                id = int(input('Введите id магазина: '))
                if product.place_get_all()[0]["id"] <= id <= product.place_get_all()[-1]["id"]:
                    shop.shops_delete_one_by_id(id)
                else:
                    print('Такого магазина не существует')

    except:
        print('')
