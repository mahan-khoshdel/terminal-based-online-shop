# README — Online Shop Data Model
## Introduction
This project involves implements an online shop system in the **data model**.
In this model, the main entities of the system which include customer, seller, product, shopping cart, order, wallet, etc. are defined as Python classes.

This file actually defines **data structure and relationships** and can be used in later stages to implement purchasing logic, manage orders, connect to the database, and design the user interface (UI) logic.

---
## File Structure
All system classes are defined in a single Python file.
They currently include constructor methods (`__init__`) but no business logic or operational methods.

---
# Class Descriptions
## Item
### **Purpose**
Represents a seller-specific offer on a product.
In stores, a "product" is usually the same thing, but "different sellers" can offer it at different prices, different quantities, and different conditions.
### **How it works**
* Connects a **Product** to a **Seller**
* Used in shopping baskets and orders
* Stores inventory price and information
### **Use Case**
Seller A sells "Laptop X" for 900.\
Seller B sells the same laptop for 870.\
These are two different **Item** objects.
### **Fields**
| Field    | Description                                     |
| -------- | ----------------------------------------------- |
| `number` | Quantity of this item available or selected.    |
| `type`   | The `Product` object that this item belongs to. |
| `price`  | Unit price of the product set by the seller.    |
---
## Seller
### **Purpose**
Represents a seller who offers products through Items.
### **How it works**
* Maintains a wallet
* Receives and manages orders
* Manages a list of item offers
* Has a rating system based on customer feedback
* Can be approved or rejected by the system operator

### **Use Case**
A seller lists multiple items, receives orders, and sees income deposited into their wallet.
### **Fields**
| Field         | Description                                                     |
| ------------- | --------------------------------------------------------------- |
| `products`    | List of `Item` objects offered by the seller.                   |
| `place`       | Physical location of the seller (used for delivery estimation). |
| `score`       | Seller’s rating based on customer feedback and performance.     |
| `order_list`  | List of orders associated with this seller.                     |
| `wallet`      | Wallet balance of the seller.                                   |
| `statistics`  | Sales statistics such as total revenue or number of sales.      |
| `user_number` | Unique seller identifier.                                       |
---
## Transaction
### **Purpose**
Represents a financial action performed on a wallet.
### **How it works**
Every deposit, withdrawal, or purchase creates a new `Transaction` object.
### **Use Case**
Customer adds funds → transaction
Customer purchases an item → transaction
### **Fields**
| Field             | Description                                |
| ----------------- | ------------------------------------------ |
| `time`            | Date of the transaction.                   |
| `tracking_number` | Tracking code to identify the transaction. |
| `amount`          | Transaction amount (positive or negative). |
---
## Wallet
### **Purpose**
Represents a digital financial account for a customer or seller.
Payments and earnings are made through the Wallet, not directly.
### **How it works**
* Used to process purchases
* Stores transaction history
* Tracks balance through transactions

### **Use Case**
The customer must add money to the wallet before making a purchase.
### **Fields**
| Field          | Description                                           |
| -------------- | ----------------------------------------------------- |
| `code`         | Unique wallet ID.                                     |
| `transactions` | List of `Transaction` objects recorded in the wallet. |
---
## Customer
### **Purpose**
Represents a user who interacts with the online shop, makes purchasing decisions, and completes purchases.
### **How it works**
* Leaves comments on products
* Stores shopping basket data
* Uses wallet to finalize purchases
* Stores personally identifiable information

### **Use Case**
A customer selects items → adds them to basket → make purchase → order recorded.
### **Fields**
| Field             | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| `name`            | Customer’s first name.                                     |
| `family`          | Customer’s last name.                                      |
| `id`              | Unique customer identifier.                                |
| `shopping_basket` | List of `Shoppingbasket` entries selected before checkout. |
| `wallet`          | Customer’s associated `Wallet`.                            |
---
## Comment
### **Purpose**
Represents a review written by a customer for a product.
### **How it works**
* Links to a product
* Contains text, timestamp, and author
* Helps other customers evaluate the quality of the product

### **Use Case**
A user writes a review:
*"Fast shipping, great quality."*
### **Fields**
| Field     | Description                           |
| --------- | ------------------------------------- |
| `context` | Text of the comment.                  |
| `time`    | Date the comment was submitted.       |
| `user`    | The `Customer` who wrote the comment. |
---
## Product
### **Purpose**
Represents an independent product in the store, regardless of how many sellers offer it.
### **How it works**
* Keeps all user comments
* Serves as a base for seller-specific versions (Items)
* Identified by unique product ID

### **Use Case**
Product “PR2030 — Gaming Mouse”
Different sellers offer Items of this product.
### **Fields**
| Field      | Description                                            |
| ---------- | ------------------------------------------------------ |
| `id`       | Unique product identifier.                             |
| `comments` | List of `Comment` objects associated with the product. |
---
## Discountcode
### **Purpose**
Represents a promotional discount code that is applied to a customer's purchase under certain conditions.
### **How it works**
* Has a time and usage limit
* May only apply to specific products
* May be limited to certain customers

### **Use Case**
10% discount code is only available to VIP customers until a specific date.
### **Fields**
| Field       | Description                                           |
| ----------- | ----------------------------------------------------- |
| `time`      | Expiration date or active date of the discount code.  |
| `customers` | List of customers eligible to use the discount code.  |
| `product`   | Product that the discount applies to (if restricted). |
| `limit`     | Maximum number of times the code may be used.         |
---
## Shoppingbasket
### **Purpose**
Represents temporary shopping cart for a customer before finalizing an order.
### **How it works**
* Applies discount codes
* Holds quantity and seller information
* Converts to `Orderlist` after checkout

### **Use Case**
User adds 2 items from seller B with one discount code applied.
### **Fields**
| Field            | Description                                  |
| ---------------- | -------------------------------------------- |
| `number`         | Quantity of the selected item.               |
| `product`        | Seller that provides the selected item.      |
| `price`          | The associated `Item` for this basket entry. |
| `discount_codes` | List of applied discount codes.              |
---
## Shop
### **Purpose**
Represents the entire structure of the online shop nd includes all the data in the system.
### **How it works**
Acts as a container for all shop-level data:
* Sellers
* Products
* Customers
* Discount codes

Future implementations may turn this class into a system-wide manager (Singleton).
### **Fields**
| Field            | Description                                |
| ---------------- | ------------------------------------------ |
| `sellers`        | List of all sellers in the shop.           |
| `products`       | List of products available.                |
| `customers`      | List of registered customers.              |
| `discount_codes` | List of discount codes active in the shop. |
---
## Orderlist
### **Purpose**
Represents a finalized and confirmed order placed by a customer.
### **How it works**
* Stores the purchased item
* Tracks seller responsibility
* Stores timestamp and discount applied
* Used for order history, delivery tracking, and seller analytics

### **Use Case**
Customer purchases an item → order is created → stored for both customer and seller dashboards.
### **Fields**
| Field           | Description                                 |
| --------------- | ------------------------------------------- |
| `id`            | Unique order identifier.                    |
| `sellers`       | Seller associated with the order.           |
| `item`          | The `Item` that was purchased.              |
| `order_time`    | Timestamp of when the order was created.    |
| `discount_code` | Discount code applied to the order, if any. |
---
## Methods
This section describes the constructor (`__init__`) and string representation (`__str__`) methods defined in each class.\
Constructors are used to create relationships between entities and initialize object properties, while `__str__` provides a readable string representation of the objects.\
At the current level of development, no full business logic methods (such as checkout, payment processing, or order lifecycle management) have been implemented yet.

---
### **Item**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `number, type, price` | Initializes item quantity, product reference, and unit price. |
| `__str__()` | — | Returns a readable string of the item. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `number` | Quantity of product. |
| `type` |  Reference to the related `Product`. |
| `price` | The unit price set by seller. |

**`__init__` Purpose:**
Creates an item instance that associates a product with seller-specific pricing and inventory information.

---
### **Seller**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `products, place, score, order_list, wallet, statistics, user_number` | Creates a seller account. |
| `__str__()` | — | Returns seller information in string format. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `products` | List of seller Items. |
| `place` | Seller location. |
| `score` | Seller rating. |
| `order_list` | List of orders. |
| `wallet` | Seller wallet balance. |
| `statistics` | Sales statistics. |
| `user_number` | Seller unique identifier. |


**`__init__` Purpose:**
Creates a seller with product catalog, financial data, and performance metrics.

---
### **Transaction**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `time, tracking_number, amount` | Creates a transaction record. |
| `__str__()` | — | Returns transaction details as string. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `time` | Date and time of transaction. |
| `tracking_number` | Unique tracking code. |
| `amount` | Transaction amount (positive or negative). |

**`__init__` Purpose:**
Represents a single financial transaction in a wallet.

---
### **Wallet**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `code, transactions` | Creates a wallet with transaction history. |
| `__str__()` | — | Returns wallet info as string. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `code` | Wallet identifier. |
| `transactions` | List of wallet transactions. |

**`__init__` Purpose:**
Creates a digital wallet that stores transaction history.

---
### **Customer**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `name, family, id, shopping_basket, wallet` | Creates a customer profile. |
| `__str__()` | — | Returns customer details as string. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `name` | Customer first name. |
| `family` | Customer last name. |
| `id` | Unique customer identifier. |
| `shopping_basket` | Basket items. |
| `wallet` | Wallet instance. |

**`__init__` Purpose:**
Creates a customer with identity, basket, and wallet data.

---
### **Comment**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `context, time, user` | Creates a product comment. |
| `__str__()` | — | Returns comment as string. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `context` | Comment text. |
| `time` | Comment date. |
| `user` | Author of the comment. |

**`__init__` Purpose:**
Stores customer feedback related to a product.

---
### **Product**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `id, comments` | Creates a product. |
| `__str__()` | — | Returns product info as string. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `id` | Product unique identifier. |
| `comments` | Product comments. |

**`__init__` Purpose:**
Creates a product entity independent of sellers.

---
### **Discountcode**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `time, customers, product, limit` | Creates discount code. |
| `__str__()` | — | Returns discount code info. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `time` | Expiration or activation date. |
| `customers` | Allowed customers. |
| `product` | Target product. |
| `limit` | Usage limit. |

**`__init__` Purpose:**
Defines a promotional discount with limitations.

---
### **Shoppingbasket**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `number, product, price, discount_codes` | Creates basket entry. |
| `__str__()` | — | Returns basket data as string. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `number` | Selected quantity. |
| `product` | Seller providing the item. |
| `price` | Related Item. |
| `discount_codes` | Applied discount codes. |

**`__init__` Purpose:**
This represents a temporary purchase option before payment.

---
### **Shop**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `sellers, products, customers, discount_codes` | Initializes shop container. |
| `__str__()` | — | Returns shop info as string. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `sellers` | All sellers. |
| `products` | All products. |
| `customers` | All customers. |
| `discount_codes` | All discount codes. |

**`__init__` Purpose:**
It acts as the central structure that holding all the system data.

---
### **Orderlist**

### Methods

| Method | Parameters | Description |
|--------|-----------|-------------|
| `__init__()` | `id, sellers, item, order_time, discount_code` | Creates order record. |
| `__str__()` | — | Returns order info as string. |

#### `__init__` Parameters

| Parameter | Description |
|----------|-------------|
| `id` | Order identifier. |
| `sellers` | Seller responsible. |
| `item` | Purchased item. |
| `order_time` | Time of order. |
| `discount_code` | Applied discount code. |

**`__init__` Purpose:**.

It represents a completed purchase and serves as an order record.

---
### Possible Future Extensions

This data model currently focuses on the core structural representation.
In future stages, this system could be extended with:

- Implementing full business logic such as checkout, payment processing, and refund management
- Adding order status tracking and delivery workflow
- Connecting to persistent storage (database integration)
- Developing a graphical or web-based user interface
- Applying role-based access control and authentication

---
# Menu System
This project provides a **multi-level terminal-based menu system** that simulates a real online shopping experience.
The system supports three main user roles:
* Customer
* Seller
* Operator (System Administrator)

Each role has its own multi-layered control panel.

---
## Root Menu
| Option   | Description                                 |
| -------- | ------------------------------------------- |
| Login    | Enter the role selection menu               |
| Register | Register a new user                         |
| Exit     | Terminating the program                     |
---
## Role Selection Menu
| Option   | Description                  |
| -------- | ---------------------------- |
| Customer | Enter customer panel         |
| Seller   | Enter seller panel           |
| Operator | Enter operator (admin) panel |
| Back     | Return to root menu          |
---
# Customer Panel
## Customer Main Menu
| Option   | Description                       |
| -------- | --------------------------------- |
| Products | Product browsing and searching    |
| Basket   | Shopping basket management        |
| Wallet   | Wallet and transaction management |
| Orders   | View order history                |
| Profile  | Customer profile management       |
| Back     | Return to role menu               |
---
### Customer → Products
| Option                | Description                    |
| --------------------- | ------------------------------ |
| View All Products     | Display all available products |
| Search Product        | Search products by ID          |
| View Product Comments | Display product reviews        |
| Back                  | Return to customer menu        |
---
### Customer → Basket
| Option          | Description                         |
| --------------- | ----------------------------------- |
| Current Basket  | View selected items                 |
| Add Item        | Add item to basket                  |
| Remove Item     | Remove item from basket             |
| Change Quantity | Change the number of selected items |
| Apply Discount  | Apply discount code                 |
| Clear Basket    | Remove all items                    |
| Back            | Return to customer menu             |
---
### Customer → Wallet
| Option              | Description                     |
| ------------------- | ------------------------------- |
| Charge Wallet       | Add money to wallet             |
| Withdraw            | Withdraw money                  |
| View Balance        | View wallet balance             |
| Transaction History | View wallet transaction list    |
| Back                | Return to customer menu         |
---
### Customer → Orders
| Option           | Description             |
| ---------------- | ----------------------- |
| Current Orders   | View active orders      |
| Completed Orders | View previous orders    |
| Cancel Order     | Cancel an order         |
| Order Details    | View full order details |
| Back             | Return to customer menu |
---
### Customer → Profile
| Option          | Description                  |
| --------------- | ---------------------------- |
| View Profile    | Display personal information |
| Edit Profile    | Modify profile information   |
| Change Password | Change login password        |
| Back            | Return to customer menu      |
---
# Seller Panel
## Seller Main Menu
| Option     | Description              |
| ---------- | ------------------------ |
| My Items   | Manage listed items      |
| Orders     | Manage received orders   |
| Wallet     | Seller wallet management |
| Statistics | View sales reports       |
| Back       | Return to role menu      |
---
### Seller → My Items
| Option      | Description              |
| ----------- | ------------------------ |
| View Items  | Show listed items        |
| Add Item    | Add new product          |
| Edit Item   | Modify price or quantity |
| Remove Item | Remove product           |
| Back        | Return to seller menu    |
---
### Seller → Orders
| Option           | Description           |
| ---------------- | --------------------- |
| Current Orders   | View active orders    |
| Completed Orders | View delivered orders |
| Cancel Order     | Cancel an order       |
| Back             | Return to seller menu |
---
### Seller → Wallet
| Option              | Description                 |
| ------------------- | --------------------------- |
| View Balance        | Display wallet balance      |
| Withdraw            | Withdraw earnings           |
| Transaction History | Display wallet transactions |
| Back                | Return to seller menu       |
---
### Seller → Statistics
| Option            | Description                |
| ----------------- | -------------------------- |
| Total Sales       | View total number of sales |
| Total Income      | View total income          |
| Most Sold Product | View best selling item     |
| Back              | Return to seller menu      |
---
# Operator Panel
## Operator Main Menu
| Option         | Description         |
| -------------- | ------------------- |
| Sellers        | Seller management   |
| Customers      | Customer management |
| Orders         | Order monitoring    |
| Discount Codes | Discount management |
| System         | System control      |
| Back           | Return to role menu |
---
### Operator → Sellers
| Option         | Description             |
| -------------- | ----------------------- |
| View Sellers   | Display sellers         |
| Confirm Seller | Verify new sellers      |
| Block Seller   | Block sellers           |
| Remove Seller  | Remove seller           |
| Back           | Return to operator menu |
---
### Operator → Customers
| Option           | Description             |
| ---------------- | ----------------------- |
| View Customers   | Display customers       |
| Confirm Customer | Verify new customers    |
| Block Customer   | Block customers         |
| Remove Customer  | Remove customers        |
| Back             | Return to operator menu |
---
### Operator → Orders
| Option          | Description             |
| --------------- | ----------------------- |
| View All Orders | Show all orders         |
| Cancel Order    | Cancel any order        |
| Search Order    | Search orders by ID     |
| Back            | Return to operator menu |
---
### Operator → Discount Codes
| Option      | Description             |
| ----------- | ----------------------- |
| Create Code | Create discount code    |
| Remove Code | Remove discount code    |
| View Codes  | Show discount codes     |
| Back        | Return to operator menu |
---
### Operator → System
| Option            | Description                |
| ----------------- | -------------------------- |
| System Statistics | View full system report    |
| Backup Data       | Create system backup       |
| Restore Data      | Restore saved data         |
| Reset System      | Reset all data             |
| Back              | Return to operator menu    |
---
## Menu Flow Overview
```
Root → Role → Customer → Basket → Checkout → Orderlist
             Seller   → Orders
             Operator → System Control
```
---
## Why This Menu Matters
This menu system turns the project from a static data model to a fully interactive online shop simulation.

It provides:

• Role-based access control
• Order lifecycle management   
• Real-time purchasing workflow   
• Wallet-based payment simulation  
• Administrative supervision  

This structure makes the project suitable for future development to a web-based or GUI-based online shop system.

---
# Conclusion
This data model file defines all the structures necessary to implement an online shop application.
This file provides the foundational layer for:
* Business logic
* Purchase workflow
* Payment and transactions
* Seller and customer operations
* Database storage
* User interface (UI) development
  
This model can be extended with methods, status tracking, and full application logic in later stages of development.