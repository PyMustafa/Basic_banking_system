# Basic Banking System

## INDEX

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Screenshots](#screenshots)

## Description

- The Basic Banking System is a web application developed using Django.
- The project simulates a simple banking system where users can view a list of customers, transfer money between customers, **import customers from an existing (CSV, JSON, Excel) file** and view transaction history.
- The project includes two main tables, 'customer' and 'transaction,' which contain relevant details.
- The website is responsive, compatible with various browsers, and mobile/tablet-friendly.

## Requirements

- Python 3.11
- Django 4.2.5
- A modern web browser (Chrome recommended)

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/Basic_banking_system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Basic_banking_system
   ```
3. Create and activate a virtual environment using 'pipenv':
   ```bash
   pipenv install
   pipenv shell
   ```
   This will create a virtual environment and install the required Python packages specified in the Pipfile
4. Make migrations and apply them to create the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create a superuser to access the Django admin panel (follow the prompts):
   ```bash
   python manage.py createsuperuser
   ```
6. Start the development server:
   ```bash
   python manage.py runserver
   ```
7. Access the admin panel at http://localhost:8000/admin/ and log in using the superuser credentials
   or Access the application at http://localhost:8000/ in your web browser and start development.

## Screenshots

- Home Page
![image](https://github.com/pyMustafa/Basic_banking_system/assets/31818881/499f3435-379d-4c33-a854-72fa7d005941)
![image](https://github.com/user-attachments/assets/eb035051-81a4-487a-bad0-ad5cc552997f)

- All Accounts
![image](https://github.com/user-attachments/assets/0bc6aad8-758e-4ea7-8242-392642e858ef)

- account information
![image](https://github.com/user-attachments/assets/404554d4-a90f-4ebc-b825-3455a19a0576)

- Transfer funds between two accounts
![image](https://github.com/user-attachments/assets/3bf88795-8767-45b0-9c7a-56eec28fbf4b)

- Transactions History
![image](https://github.com/user-attachments/assets/dc7fd93d-a8a9-4d84-a9e5-582c4e541f64)





