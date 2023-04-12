import csv


def create_index(my_data: list, column_name: str):
    """
    Функция создаёт индекс по колонке.
    :param my_data: список словарей, каждый элемент списка имеет одинаковые ключи.
    :param column_name: имя ключа, по которому делать индекс.
    :return: индекс.
    """
    my_index = dict()
    for item in my_data:
        if item[column_name] not in my_index:
            my_index[item[column_name]] = list()
        my_index[item[column_name]].append(item)
    return my_index


#  Функция, которая выводит статистику по каждому бренду.
def print_brand_stats(my_index):
    for brand, items in my_index.items():
        print(f"Від бренду '{brand}' є {len(items)} товарів")


#  Функция, которая выводит статистику по каждой категории.
def print_category_stats(my_index):
    for category, items in my_index.items():
        print(f"Серед категорії '{category}' є {len(items)} товарів")


#  Функция, которая выводит всю информацию по определенному бренду.
def print_brand_items(my_index, brand):
    print(f"Бренд '{brand}':")
    for item in my_index[brand]:
        if item['brand'] == brand:
            print(item)


#  Функция, которая выводит всю информацию по определенной категории товара.
def print_category_items(my_index, category):
    print(f"Категорія '{category}':")
    for item in my_index[category]:
        if item['category'] == category:
            print(item)


#  Функция, которая выводит информацию по брендам и их количеству в категориях товара.
def print_brand_category_distribution(my_index):
    for category, items in my_index.items():
        brand_count = {}
        for item in items:
            brand = item['brand']
            if brand not in brand_count:
                brand_count[brand] = 0
            brand_count[brand] += 1
        print(f"У категорії '{category}' представлені товари таких брендів: {brand_count}")


if __name__ == '__main__':
    # відкриваємо файл для читання
    with open('tech_inventory.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        # зберігаємо дані у список списків
        data = list(reader)

    brand_index = create_index(data, 'brand')
    print('=' * 70)
    print_brand_stats(brand_index)
    category_index = create_index(data, 'category')
    print('=' * 70)
    print_category_stats(category_index)
    print('=' * 70)
    print_brand_items(brand_index, 'Apple')
    print('=' * 70)
    print_category_items(category_index, 'Laptop')
    print('=' * 70)
    print_brand_category_distribution(category_index)
