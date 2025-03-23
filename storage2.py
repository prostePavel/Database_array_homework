products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "price": 30,
        "name": "BMW",
    },
    {
        "price": 30,
        "name": "Lambo",
    }
]


def print_products():
    for product in products:
        print(f"Název produktu2: {product['name']}, cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu:")
    product_price = input("Název cenu:")
    product2 = {
        'name': product_name,
        'price': product_price
    }

    products.append(product2)


def cheapest_product():
    cheapest_items = cheapest_item(products)

    for item in cheapest_items:
        print(f"{item['name']}, cena: {item['price']}$")

    menu()


def cheapest_item(items):
    min_price = min(item['price'] for item in items)
    return [item for item in items if item['price'] == min_price]




def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis polože")
    print("2. Přidání položky")
    print("3. Zobrazit nejlevnější produkt\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání poožky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("nejlevnější produkt je:")
        cheapest_product()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
