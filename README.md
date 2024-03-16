# Asset Management Software


## Overview

The Asset Management Software is a web application designed to help businesses manage their assets efficiently. It provides features for inventory management, finance management, intangible assets tracking, machinery management, vehicle management, hardware and software tracking, furniture management, supply chain management, investments tracking, fixed assets management, and contract management. The application is built using Django for the backend and React for the frontend.

## Features

- **Inventory Management**: Track and manage inventory across various industries and categories.
- **Finance Management**: Manage finances, expenses, savings, budgets, and investments.
- **Intangible Assets**: Track intangible assets such as licenses, copyrights, trademarks, policies, and agreements.
- **Machinery Management**: Track and manage machinery across different industries and categories.
- **Vehicle Management**: Track and manage vehicles with details such as registration, purchase date, and maintenance records.
- **Hardware and Software Tracking**: Track computer hardware and software assets with warranty details and documentation.
- **Furniture Management**: Track furniture assets with warranty details and maintenance records.
- **Supply Chain Management**: Manage various aspects of the supply chain including stock notifications and purchasing processes.
- **Investments Tracking**: Track investments across different categories such as stocks, bonds, mutual funds, and cryptocurrencies.
- **Fixed Assets Management**: Track fixed assets such as land, buildings, and houses with warranty and maintenance records.
- **Contract Management**: Track contracts with details such as expiry dates, values, and documentation.

## Technologies Used

- **Backend**: Django, MariaDB
- **Frontend**: React
- **Database**: MariaDB (MySQL)
- **Blockchain Integration**: [Blockchain Technology Name]

## Installation

1. Clone the repository:
   ```bash
   git clone <https://github.com/IsmaelKiprop/asset-manager-app.git>

## Setting Up the Backend and Database

To set up the backend and configure the database for the Asset Management Software, follow these steps:

1. **Navigate to the Backend Directory:**
   ```bash
   cd backend

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

3. **Set Up MariaDB:**
   
Install MariaDB on your server or local machine. You can download it from MariaDB Downloads.Start the MariaDB server using appropriate commands for your operating system.Access the MariaDB shell using the command:
```bash
mysql -u root -p
```
- **Create a database for the application**
```bash
CREATE DATABASE asset_management_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
- **Create a user for the database**
```bash
CREATE USER 'assets'@'localhost' IDENTIFIED BY 'assets';
```
- **Grant all privileges to the user on the database**
```bash
GRANT ALL PRIVILEGES ON asset_management_db.* TO 'assets'@'localhost';
```
- **Flush privileges to apply changes**
```bash
FLUSH PRIVILEGES;
```
4. **Run migrations:**
   ```bash
   python manage.py migrate

5. **Start the Django development server:**
   ```bash
   python manage.py runserver
   ```
- **Access your application at:**
  ```bash
  http://localhost:8000/api/v1
  ```
6. **Navigate to the frontend directory:**
   ```bash
   cd frontend

7. **Install dependencies:**
   ```bash
   npm install

8. **Start the React development server:**
   ```bash
   npm start

9. **Access the application in your web browser at:**
```bash
http://localhost:3000.
```

## Contributing

Contributions are welcome! Please follow the contribution guidelines to contribute to this project.

## License

This project is licensed under the MIT License.
