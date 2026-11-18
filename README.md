# Inventory Management System

A Python-based Inventory Management System designed to manage products, track stock levels, handle sales and restocking operations, and monitor product expiration dates.

This project demonstrates the practical application of Object-Oriented Programming (OOP) concepts in Python.

## Features

- Add products to the inventory.
- Restock existing products.
- Sell products and update stock quantities.
- Prevent selling products when stock is insufficient.
- Manage perishable products with expiration dates.
- Prevent selling expired products.
- Generate low-stock alerts.
- Generate inventory reports with total products and stock quantities.
- Validate product prices and stock values.

## OOP Concepts Implemented

This project applies several core OOP concepts:

- **Classes and Objects:** Creating Product, PerishableProduct, and Inventory classes.
- **Encapsulation:** Using private-style attributes with properties and setters to validate stock and price values.
- **Inheritance:** PerishableProduct inherits from the Product class.
- **Polymorphism:** Overriding methods such as `remove_stock()` and `__str__()` in the child class.
- **Method Overriding:** Providing specialized behavior for perishable products.
- **Constructor (`__init__`):** Initializing objects and their attributes.
- **`super()`:** Reusing parent class methods and constructors.
- **Magic Methods:** Using `__str__()` to provide readable object representations.
- **`isinstance()`:** Checking product types when generating inventory reports.

## Technologies Used

- Python
- Object-Oriented Programming (OOP)
- datetime module

## Project Structure

```text
Inventory-Management-System/
│
├── Inventory_management_system.py
└── README.md
```

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open the project folder in VS Code.
4. Run the following command:

```bash
python Inventory_management_system.py
```

The script runs sample operations demonstrating product creation, inventory management, restocking, selling, low-stock alerts, and report generation.

## Learning Objectives

The main goal of this project is to strengthen practical Python OOP skills by building a small inventory management system with reusable classes, validation, inheritance, and real-world business logic.

## Author

Zeyad Ahmed Mohamed
