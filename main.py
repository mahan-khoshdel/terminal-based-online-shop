import datetime


class Item:
    number: int = 0
    type: "Product" = None
    price: int = 0

    def __init__(self, number, type, price):
        self.number = number
        self.type = type
        self.price = price

    def __str__(self):
        return f"number:{self.number},type:{self.type},price:{self.price}"


class Seller:
    products: list[Item]
    place: str = ""
    score: int = 0
    order_list: list["Orderlist"]
    wallet: int = 0
    statistics: int = 0
    user_number: str = ""

    def __init__(self, products, place, score, order_list, wallet, statistics, user_number):
        self.products = products
        self.place = place
        self.score = score
        self.order_list = order_list
        self.wallet = wallet
        self.statistics = statistics
        self.user_number = user_number

    def __str__(self):
        return f"products:{self.products},place:{self.place},score:{self.score},order_list:{self.order_list},wallet:{self.wallet},statistics:{self.statistics},user_number:{self.user_number}"


class Transaction:
    time: datetime.datetime
    tracking_number: int = 0
    amount: int = 0

    def __init__(self, time, tracking_number, amount):
        self.time = time
        self.tracking_number = tracking_number
        self.amount = amount

    def __str__(self):
        return f"time:{self.time},tracking_number:{self.tracking_number},amount:{self.amount}"


class Wallet:
    code: int = 0
    transactions: list[Transaction]

    def __init__(self, code, transactions):
        self.code = code
        self.transactions = transactions

    def __str__(self):
        return f"code:{self.code},transactions:{self.transactions}"


class Customer:
    name: str = ""
    family: str = ""
    id: str = ""
    shopping_basket: list["Shoppingbasket"]
    wallet: Wallet = None

    def __init__(self, name, family, id, shopping_basket, wallet):
        self.name = name
        self.family = family
        self.id = id
        self.shopping_basket = shopping_basket
        self.wallet = wallet

    def __str__(self):
        return f"name:{self.name},family:{self.family},id:{self.id},shopping_basket:{self.shopping_basket},wallet:{self.wallet}"


class Comment:
    context: str = ""
    time: datetime.datetime
    user: Customer = None

    def __init__(self, context, time, user):
        self.context = context
        self.time = time
        self.user = user

    def __str__(self):
        return f"context:{self.context},time:{self.time},user:{self.user}"


class Product:
    id: str = ""
    comments: list[Comment]

    def __init__(self, id, comments):
        self.id = id
        self.comments = comments

    def __str__(self):
        return f"id:{self.id},comments:{self.comments}"


class Discountcode:
    time: datetime.datetime
    customers: list[Customer]
    product: Product = None
    limit: int = 0

    def __init__(self, time, customers, product, limit):
        self.time = time
        self.customers = customers
        self.product = product
        self.limit = limit

    def __str__(self):
        return f"time:{self.time},customers:{self.customers},product:{self.product},limit:{self.limit}"


class Shoppingbasket:
    number: int = 0
    product: Seller = None
    price: Item = None
    discount_codes: list[Discountcode]

    def __init__(self, number, product, price, discount_codes):
        self.number = number
        self.product = product
        self.price = price
        self.discount_codes = discount_codes

    def __str__(self):
        return f"number:{self.number},product:{self.product},price:{self.price},discount_codes:{self.discount_codes}"


class Shop:
    sellers: list[Seller]
    products: list[Product]
    customers: list[Customer]
    discount_codes: list[Discountcode]

    def __init__(self, sellers, products, customers, discount_codes):
        self.sellers = sellers
        self.products = products
        self.customers = customers
        self.discount_codes = discount_codes

    def __str__(self):
        return f"sellers:{self.sellers},products:{self.products},customers:{self.customers},discount_codes:{self.discount_codes}"


class Orderlist:
    id: str = ""
    sellers: Seller = None
    item: Item = None
    order_time: datetime.datetime
    discount_code: Discountcode = None

    def __init__(self, id, sellers, item, order_time, discount_code):
        self.id = id
        self.sellers = sellers
        self.item = item
        self.order_time = order_time
        self.discount_code = discount_code

    def __str__(self):
        return f"id:{self.id},sellers:{self.sellers},item:{self.item},order_time:{self.order_time},discount_code:{self.discount_code}"


level = "root"
while True:
    if level == "root":
        print("1.login")
        print("2.register")
        print("3.exit")
        cmd = int(input(">>"))
        if cmd == 1:
            level = "login"
        elif cmd == 2:
            level = "register"
        elif cmd == 3:
            break

    elif level == "login":
        print("1.operator")
        print("2.seller")
        print("3.customer")
        print("4.back")
        cmd = int(input(">>"))
        if cmd == 1:
            level = "operator"
        if cmd == 2:
            level = "seller"
        if cmd == 3:
            level = "customer"
        if cmd == 4:
            level = "root"

    elif level == "operator":
        print("1.sellers")
        print("2.customers")
        print("3.orders")
        print("4.discount codes")
        print("5.system")
        print("6.back")
        cmd = int(input(">>"))
        if cmd == 1:
            level = "op_sellers"
        if cmd == 2:
            level = "op_customers"
        if cmd == 3:
            level = "op_orders"
        if cmd == 4:
            level = "op_discounts"
        if cmd == 5:
            level = "op_system"
        if cmd == 6:
            level = "login"

    elif level == "op_sellers":
        print("1.view sellers")
        print("2.confirm seller")
        print("3.block seller")
        print("4.remove seller")
        print("5.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Showing all registered sellers...")
        if cmd == 2:
            print("Seller confirmation process started.")
        if cmd == 3:
            print("Seller has been blocked.")
        if cmd == 4:
            print("Seller removed from system.")
        if cmd == 5:
            level = "operator"

    elif level == "op_customers":
        print("1.view customers")
        print("2.confirm customer")
        print("3.block customer")
        print("4.remove customer")
        print("5.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Showing all registered customers...")
        if cmd == 2:
            print("Customer confirmation completed.")
        if cmd == 3:
            print("Customer blocked.")
        if cmd == 4:
            print("Customer removed from system.")
        if cmd == 5:
            level = "operator"

    elif level == "op_orders":
        print("1.view all orders")
        print("2.cancel order")
        print("3.search order")
        print("4.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Displaying all system orders...")
        if cmd == 2:
            print("Order cancellation requested.")
        if cmd == 3:
            print("Order search started.")
        if cmd == 4:
            level = "operator"

    elif level == "op_discounts":
        print("1.create code")
        print("2.remove code")
        print("3.view codes")
        print("4.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Creating a new discount code...")
        if cmd == 2:
            print("Discount code removed.")
        if cmd == 3:
            print("Displaying all discount codes...")
        if cmd == 4:
            level = "operator"

    elif level == "op_system":
        print("1.system statistics")
        print("2.backup data")
        print("3.restore data")
        print("4.reset system")
        print("5.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("System statistics are being calculated...")
        if cmd == 2:
            print("System backup created.")
        if cmd == 3:
            print("System data restored.")
        if cmd == 4:
            print("System reset successfully.")
        if cmd == 5:
            level = "operator"

    elif level == "seller":
        print("1.my items")
        print("2.orders")
        print("3.wallet")
        print("4.statistics")
        print("5.back")
        cmd = int(input(">>"))
        if cmd == 1:
            level = "seller_items"
        if cmd == 2:
            level = "seller_orders"
        if cmd == 3:
            level = "seller_wallet"
        if cmd == 4:
            level = "seller_statistics"
        if cmd == 5:
            level = "login"

    elif level == "seller_items":
        print("1.view items")
        print("2.add item")
        print("3.edit item")
        print("4.remove item")
        print("5.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Displaying your items...")
        if cmd == 2:
            print("Add new item process started.")
        if cmd == 3:
            print("Edit item process started.")
        if cmd == 4:
            print("Item removed.")
        if cmd == 5:
            level = "seller"

    elif level == "seller_orders":
        print("1.current orders")
        print("2.completed orders")
        print("3.cancel order")
        print("4.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Showing current orders...")
        if cmd == 2:
            print("Showing completed orders...")
        if cmd == 3:
            print("Order cancellation sent.")
        if cmd == 4:
            level = "seller"

    elif level == "seller_wallet":
        print("1.view balance")
        print("2.withdraw")
        print("3.transaction history")
        print("4.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Your current balance is displayed.")
        if cmd == 2:
            print("Withdraw request submitted.")
        if cmd == 3:
            print("Transaction history displayed.")
        if cmd == 4:
            level = "seller"

    elif level == "seller_statistics":
        print("1.total sales")
        print("2.total income")
        print("3.most sold product")
        print("4.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Total sales calculated.")
        if cmd == 2:
            print("Total income calculated.")
        if cmd == 3:
            print("Most sold product identified.")
        if cmd == 4:
            level = "seller"

    elif level == "customer":
        print("1.products")
        print("2.basket")
        print("3.wallet")
        print("4.orders")
        print("5.profile")
        print("6.back")
        cmd = int(input(">>"))
        if cmd == 1:
            level = "cust_products"
        if cmd == 2:
            level = "cust_basket"
        if cmd == 3:
            level = "cust_wallet"
        if cmd == 4:
            level = "cust_orders"
        if cmd == 5:
            level = "cust_profile"
        if cmd == 6:
            level = "login"

    elif level == "cust_products":
        print("1.view all products")
        print("2.search product")
        print("3.view product comments")
        print("4.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Showing all products...")
        if cmd == 2:
            print("Product search started.")
        if cmd == 3:
            print("Displaying product comments...")
        if cmd == 4:
            level = "customer"

    elif level == "cust_basket":
        print("1.current basket")
        print("2.add item")
        print("3.remove item")
        print("4.change quantity")
        print("5.apply discount")
        print("6.clear basket")
        print("7.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Current basket displayed.")
        if cmd == 2:
            print("Item added to basket.")
        if cmd == 3:
            print("Item removed from basket.")
        if cmd == 4:
            print("Basket item quantity updated.")
        if cmd == 5:
            print("Discount code applied.")
        if cmd == 6:
            print("Basket cleared.")
        if cmd == 7:
            level = "customer"

    elif level == "cust_wallet":
        print("1.charge wallet")
        print("2.withdraw")
        print("3.view balance")
        print("4.transaction history")
        print("5.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Wallet charged successfully.")
        if cmd == 2:
            print("Withdraw request sent.")
        if cmd == 3:
            print("Current wallet balance displayed.")
        if cmd == 4:
            print("Wallet transaction history shown.")
        if cmd == 5:
            level = "customer"

    elif level == "cust_orders":
        print("1.current orders")
        print("2.completed orders")
        print("3.cancel order")
        print("4.order details")
        print("5.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Displaying current orders...")
        if cmd == 2:
            print("Displaying completed orders...")
        if cmd == 3:
            print("Order cancellation requested.")
        if cmd == 4:
            print("Order details displayed.")
        if cmd == 5:
            level = "customer"

    elif level == "cust_profile":
        print("1.view profile")
        print("2.edit profile")
        print("3.change password")
        print("4.back")
        cmd = int(input(">>"))
        if cmd == 1:
            print("Profile information displayed.")
        if cmd == 2:
            print("Profile edit mode enabled.")
        if cmd == 3:
            print("Password change requested.")
        if cmd == 4:
            level = "customer"
