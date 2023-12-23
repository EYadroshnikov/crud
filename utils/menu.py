def print_commands(n):
    if n == 1:
        print('Sellers commands: ')
        print('1. Sellers.id - Получить id сотрудника по имени.')
        print('2. Sellers.dismiss - Уволить сотрудника по id.')
        print('3. Sellers.employ - Нанять сотрудника.')
        print('4. Sellers.update - обновление информации.')
    if n == 2:
        print('Category commands: ')
        print('1. Category.id - Получить id категории товаров.')
        print('2. Category.del - Удалить категорию товаров.')
        print('3. Category.add - Добавить категорию товаров.')
    if n == 3:
        print('Place commands: ')
        print('Product.add - добавить новый товар')
        print('Product.cnt - получить количество продуктов')
        print('Product.get_all_in_category - получить все из категории')
    if n == 4:
        print('Shops commands: ')
        print('1. Shop.id - Получить id магазина.')
        print('2. Shop.add - Добавить магазин.')
        print('3. Shop.del - Удалить магазин.')
