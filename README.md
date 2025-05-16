# coffee-shop
This project implements a domain model for a Coffee Shop system, featuring three main entities: Customer, Coffee, and Order.

# Entity Relationships:
The domain model consists of the following relationships:

Customers can place many Orders

Coffees can appear in many Orders

Each Order belongs to exactly one Customer and one Coffee

This creates a many-to-many relationship between Customers and Coffees through the Order entity


# folder structure
├── lib/                                  
│     ├── customer.py     
│     ├── coffee.py       
│     └── order.py 