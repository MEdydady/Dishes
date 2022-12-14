import pprint

with open("dishes.txt", encoding="utf-8") as f:

    cook_book = {}
    for line in f:
        name_dish = line.strip()
        dishs_count = int(f.readline())
        dishs = []
        for i in range(dishs_count):
            dish = f.readline().strip()
            name, quantity, measured = dish.split('|')

            dishs.append({
                'ingredient_name': name,
                'quantity': int(quantity),
                'measured': measured,
            })
        f.readline()
        cook_book[name_dish] = dishs

    pprint.pprint(cook_book, width=200)
    print()


def get_shop_list_by_dishes(dishes, person_count):

    result = {}
    for x, y in cook_book.items():

        if x in dishes:

            for i in y:
                name = i.pop('ingredient_name')
                z = dict(reversed(
                    i.items()))  # Меняю местами элементы measure  и quantity
                if name in result:
                    z['quantity'] = result[name]['quantity'] + i['quantity']
                result[name] = z

    for x, y in result.items():
        y['quantity'] = y['quantity'] * person_count  #

    pprint.pprint(result)
    return


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 1)
