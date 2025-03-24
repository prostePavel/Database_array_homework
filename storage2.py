
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

def delete_product():
    delete = input("Odstranit produkt:")
    for product in products:
        if product['name'] == delete:
            products.remove(product)
            menu()


def cheapest_product():
    minimum = float("inf")
    for product in products:
        if product['price'] < minimum:
            minimum = product['price']

    print("nejlevnější produkt je:")
    for product in products:
        if minimum == product['price']:
            print(f"{product['name']}, cena: {product['price']}$")

def most_expensive_product():
    maximum = float("-inf")
    for product in products:
        if product['price'] > maximum:
            maximum = product['price']

    print("nejdražší produkt je: ")
    for product in products:
        if maximum == product['price']:
            print(f"{product['name']}, cena: {product['price']}$")


def search_products():
    print("hledat produkt: ")
    search = input("").strip().lower()

    for product in products:
        if search in product['name'].lower():
            print(f"{product['name']}, cena: {product['price']}$")
            print("Hledat znovu?")
            choice = input("(a/n)\n").strip().lower()
            if choice == "a":
                search_products()
            else:
                menu()
        else:
            print("hledaný produkt nenalezen.")
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
    print("3. odebrání položky")
    print("4. Zobrazit nejlevnější produkt")
    print("5. Zobrazit nejdražší produkt")
    print("6. Vyhledat produkt\n")

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
        print("")
        delete_product()
        print("")
        menu()

    elif choice == 4:
        print("Nejlevnější produkt je:")
        cheapest_product()
        print("")
        menu()

    elif choice == 5:
        print("Nejdražší produkt je:")
        most_expensive_product()
        print("")
        menu()

    elif choice == 6:
        print("")
        search_products()
        print("")
        menu()


    else:
        print("Zadal jsi špatně!\n")
        menu()


menu()
