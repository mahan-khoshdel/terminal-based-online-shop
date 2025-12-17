# README — Online Shop Data Model
## Introduction
This project involves implements an online shop system in the **data model**.
In this model, the main entities of the system which include customer, seller, product, shopping cart, order, wallet, etc. are defined as Python classes.

This file actually defines **data structure and relationships** and can be used in later stages to implement purchasing logic, manage orders, connect to the database, and design the user interface (UI) logic.

---
## File Structure
All system classes are defined in a single Python file and and have no methods or implementation logic. This file only specifies data types and relationships between entities.

---
# Class Descriptions
---
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
| Field    | Description                              |
| -------- | ---------------------------------------- |
| `number` | Quantity of this item available or selected.          |
| `type`   | The `Product` object that this item belongs to. |
| `price`  | Unit price of the product set by the seller.               |
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
| Field         | Description                                        |
| ------------- | -------------------------------------------------- |
| `products`    | List of `Item` objects offered by the seller.              |
| `place`       | Physical location of the seller (used for delivery estimation).                        |
| `score`       | Seller’s rating based on customer feedback and performance.                                |
| `order_list`  | List of orders associated with this seller.                     |
| `wallet`      | Wallet balance of the seller.                 |
| `staistics`   | Sales statistics such as total revenue or number of sales. |
| `user_number` | Unique seller identifier.                          |
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
| Field             | Description                              |
| ----------------- | ---------------------------------------- |
| `time`            | Date of the transaction.                 |
| `tracking_number` | Tracking code to identify the transaction.           |
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
| Field          | Description                    |
| -------------- | ------------------------------ |
| `code`         | Unique wallet ID.                     |
| `transactions` | List of `Transaction` objects recorded in the wallet. |
---
## Customer
### **Purpose**
Represents a user who interacts with the online shop, makes purchasing decisions, and completes purchases.
### **How it works**
* Stores shopping basket data
* Leaves comments on products
* Uses wallet to finalize purchases
* Stores personally identifiable information

### **Use Case**
A customer selects items → adds them to basket → make purchase → order recorded.
### **Fields**
| Field             | Description                       |
| ----------------- | --------------------------------- |
| `name`            | Customer’s first name.            |
| `family`          | Customer’s last name.             |
| `id`              | Unique customer identifier.                        |
| `shopping_basket` | List of `Shoppingbasket` entries selected before checkout. |
| `wallet`          | Customer’s associated `Wallet`.                |
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
| Field     | Description                     |
| --------- | ------------------------------- |
| `context` | Text of the comment.                   |
| `time`    | Date the comment was submitted.                |
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
| Field      | Description                       |
| ---------- | --------------------------------- |
| `id`       | Unique product identifier.                       |
| `comments` | List of `Comment` objects associated with the product. |
---
## Discountcode
### **Purpose**
Represents a promotional discount code that is applied to a customer's purchase under certain conditions.
### **How it works**
* Has a time and usage limit
* May be limited to certain customers
* May only apply to specific products

### **Use Case**
10% discount code is only available to VIP customers until a specific date.
### **Fields**
| Field       | Description                    |
| ----------- | ------------------------------ |
| `time`      | Expiration date or active date of the discount code. |
| `customers` | List of customers eligible to use the discount code.    |
| `product`   | Product that the discount applies to (if restricted).    |
| `limit`     | Maximum number of times the code may be used.          |
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
| Field            | Description               |
| ---------------- | ------------------------- |
| `number`         | Quantity of the selected item.        |
| `product`        | Seller that provides the selected item. |
| `price`          | The associated `Item` for this basket entry.    |
| `discount_codes` | List of applied discount codes.   |
---
## Shop
### **Purpose**
Represents the entire structure of the online shop nd includes all the data in the system.
### **How it works**
Acts as a container for all shop-level data:
* Sellers
* Customers
* Products
* Discount codes

Future implementations may turn this class into a system-wide manager (Singleton).
### **Fields**
| Field            | Description            |
| ---------------- | ---------------------- |
| `sellers`        | List of all sellers in the shop.       |
| `products`       | List of products available.      |
| `customers`      | List of registered customers.     |
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
| Field           | Description                     |
| --------------- | ------------------------------- |
| `id`            | Unique order identifier.        |
| `sellers`       | Seller associated with the order.    |
| `item`          | The `Item` that was purchased.                 |
| `order_time`    | Timestamp of when the order was created.         |
| `discount_code` | Discount code applied to the order, if any. |
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
  
The model can be expanded by using methods, status tracking, and full application logic in later stages of development.