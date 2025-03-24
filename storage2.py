products = [
    {
        "name": "Audi",
        "price": 50
    },
    {
        "name": "BMW",
        "price": 30,

    },
    {
        "name": "Lambo",
        "price": 30
    },
    {
        "name": "Porsche",
        "price": 50,
    }
]


def print_products():
    for product in products:
        print(f"Název produktu: {product['name']}, cena: {product['price']}$")


def add_product():
    product_name = input("Název produktu:").strip()
    product_price = int(input("Víše ceny:").strip())
    product = {
        'name': product_name,
        'price': product_price
    }

    products.append(product)


def cheapest_product():
    cheapest_items = cheapest_item(products)

    for item in cheapest_items:
        print(f"{item['name']}, cena: {item['price']}$")
    menu()

def cheapest_item(items):
    min_price = min(item['price'] for item in items)
    return [item for item in items if item['price'] == min_price]


def most_expensive_product():
    most_expensive_items = most_expensive_item(products)

    for item in most_expensive_items:
        print(f"{item['name']}, cena: {item['price']}$")
    menu()

def most_expensive_item(items):
    max_price = max(item['price'] for item in items)
    return [item for item in items if item['price'] == max_price]


def search_products():
    search = input("Vyhledat produkt: ").strip().lower()

    for product in products:
        if search in product['name'].lower():
            print(f"{product['name']}, cena: {product['price']}$")
            print("Hledat znovu?")
            choice = input("(a/n)\n").strip().lower()
            if choice == "a":
                search_products()
            else:
                menu()


def menu():
    print("Vítej ve skladu")
    print("###############\n")
    print("1. Výpis položek")
    print("2. Přidání položky")
    print("3. Zobrazit nejlevnější produkt")
    print("4. Zobrazit nejdražší produkt")
    print("5. Vyhledat produkt\n")

    choice = int(input("Volba: "))

    if choice == 1:
        print("Položky na skladě jsou:")
        print_products()
        print("")
        menu()

    elif choice == 2:
        print("Přidání položky:")
        add_product()
        print("")
        menu()

    elif choice == 3:
        print("Nejlevnější produkt je:")
        cheapest_product()
        print("")
        menu()
    elif choice == 4:
        print("Nejdražší produkt je:")
        most_expensive_product()
        print("")
        menu()
    elif choice == 5:
        print("hledat produkt:")
        search_products()
        print("")
        menu()

    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
