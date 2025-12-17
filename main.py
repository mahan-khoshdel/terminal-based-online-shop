import datetime


class Item:
    number: int = 0
    type: "Product" = None
    price: int = 0


class Seller:
    products: list[Item]
    place: str = ""
    score: int = 0
    order_list: list["Orderlist"]
    wallet: int = 0
    staistics: int = 0
    user_number: str = ""


class Transaction:
    time: datetime.datetime
    tracking_number: int = 0
    amount: int = 0


class Wallet:
    code: int = 0
    transactions: list[Transaction]


class Customer:
    name: str = ""
    family: str = ""
    id: str = ""
    shopping_basket: list["Shoppingbasket"]
    wallet: Wallet = None


class Comment:
    context: str = ""
    time: datetime.datetime
    user: Customer = None


class Product:
    id: str = ""
    comments: list[Comment]


class Discountcode:
    time: datetime.datetime
    customers: list[Customer]
    product: Product = None
    limit: int = 0


class Shoppingbasket:
    number: int = 0
    product: Seller = None
    price: Item = None
    discount_codes: list[Discountcode]


class Shop:
    sellers: list[Seller]
    products: list[Product]
    customers: list[Customer]
    discount_codes: list[Discountcode]


class Orderlist:
    id: str = ""
    sellers: Seller = None
    item: Item = None
    order_time: datetime.datetime
    discount_code: Discountcode = None
