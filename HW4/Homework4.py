class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = price
        self.quantity = quantity

    def change_price(self, new_price):
        self.price = new_price

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

    def __str__(self):
        return f'name: {self.name}, category: {self.category}, price: {self.price}, quantity: {self.quantity}'


class Customer:
    def __init__(self, name, email, orders=None):
        self.name = name
        self.email = email
        self.orders = orders or []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"user_name: {self.name}, email: {self.email}, orders: {self.orders or 'no orders yet'}"


class Order:
    def __init__(self):
        self.products = []

    def add_product(self, product, quantity):
        self.products.append((product, quantity))

    def total_price(self):
        return sum(p.price * q for p, q in self.products)


def load_products(filename="products.txt"):
    products = []
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, category, price, quantity = line.strip().split(",")
            product = Product(
                name,
                category,
                float(price),
                int(quantity)
            )
            products.append(product)
    return products


def load_customers(filename="customers.txt"):
    customers = []
    with open(filename, 'r', encoding="utf-8") as file:
        for user in file:
            user = user.strip()

            parts = user.split(",", 2)

            name, email, list_of_orders = parts
            orders_list = list_of_orders.split(";") if list_of_orders else 'Замовлень немає'

            customers.append(Customer(name, email, orders_list))

    return customers


def save_products(products, filename="products.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        for p in products:
            file.write(f"{p.name},{p.category},{p.price},{p.quantity}\n")


def save_new_customers(customers, filename="customers.txt"):
    with open(filename, "a", encoding="utf-8") as file:
        for c in customers:
            if c.orders:
                orders_str = ";".join(c.orders)
            else:
                orders_str = "замовлень немає"
            file.write(f"{c.name},{c.email},{orders_str}\n")


def test_shop():
    products = [
        Product("TeddyBear", "м'яка іграшка", 300.0, 10),
        Product("Lego", "конструктор", 1500.0, 5),
        Product("Car", "іграшкова машинка", 200.5, 20),
        Product("Doll", "лялька", 250.0, 7),
        Product("Ball", "м'яч", 100.0, 15)
    ]
    save_products(products)

    customers = [
        Customer("Олексій Петренко", "oleksiy@gmail.com"),
        Customer("Марія Коваленко", "maria@gmail.com"),
        Customer("Дмитро Іванченко", "dmitro@gmail.com"),
    ]

    order_ex = Order()
    order_ex.add_product(products[0], 2)
    order_ex.add_product(products[1], 1)
    customers[0].add_order(f"{products[0].name}:2;{products[1].name}:1 , Сума: {order_ex.total_price()} грн")

    order2 = Order()
    order2.add_product(products[2], 3)
    customers[1].add_order(f"{products[2].name}:3,  Сума: {order2.total_price()} грн")

    save_new_customers(customers)

    current_customers = load_customers()

    print("\n All clients for now: ")
    for c in current_customers:
        print(c)

    print("=" * 100)

    current_products = load_products()
    print("\n All products gor now: ")
    for p in current_products:
        print(p)


test_shop()
