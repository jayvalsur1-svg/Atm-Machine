# Python ATM Banking System

## Overview

This project is a command-line ATM Banking System built with Python. It simulates basic banking operations and stores account information in JSON files, allowing users to create accounts and perform transactions.

The project was developed to practice Object-Oriented Programming (OOP), file handling, JSON data management, and banking transaction logic.

---

## Features

* Create a new bank account
* Generate a unique account ID
* Create and change ATM PIN
* Secure PIN verification
* Check account balance
* Deposit money
* Withdraw money
* Transfer money between accounts
* Store account data in JSON files
* Persistent data storage

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* File Handling
* Random Module

---

## Project Structure

```text
project/
│
├── atm.py
├── user_account_12345.json
├── user_account_67890.json
└── README.md
```

---

## How It Works

### Account Creation

When a new user registers:

* Username is collected
* Unique Account ID is generated
* PIN is created
* Initial deposit is stored
* Account information is saved in a JSON file

### Banking Operations

After logging in, users can:

1. Create PIN
2. Change PIN
3. Check Balance
4. Withdraw Money
5. Deposit Money
6. Transfer Money

---

## Example Account Data

```json
{
    "username": "jay",
    "id": 123456789,
    "password": 1234,
    "Balance": 5000
}
```

---

## Learning Outcomes

This project helped improve understanding of:

* Python Classes and Objects
* Inheritance
* Method Design
* Data Persistence
* JSON Handling
* Banking System Logic
* Authentication Systems

---

## Future Improvements

* Exception Handling
* Transaction History
* Date and Time Logging
* Account Locking After Multiple Failed PIN Attempts
* Password Encryption
* Database Integration (SQLite/MySQL)
* GUI Version using Tkinter or PyQt
* REST API Version using FastAPI

---

## Author

Jay Valsur

Aspiring Python Developer passionate about software development, automation, AI, and backend systems.
