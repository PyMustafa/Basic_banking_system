# Basic Banking System

## INDEX

- [Description](#description)
- [LinkedIn Video Demo](#linkedin-video-demo)
- [Requirements](#requirements)
- [Installation](#installation)
- [Screenshots](#screenshots)

## Description

- The Basic Banking System is a web application developed using Django.
- This project is a part of The Sparks Foundation Graduate Rotational Internship Program (GRIP) - September 2023.
- The project simulates a simple banking system where users can view a list of customers, transfer money between customers, and view transaction history.
- The project includes two main tables, 'customer' and 'transaction,' which contain relevant details.
- The website is responsive, compatible with various browsers, and mobile/tablet-friendly.

## LinkedIn Video Demo

Check out a demo of the project on LinkedIn: [LinkedIn Video Demo](https://www.linkedin.com/posts/mustafaahassan_thesparksfoundation-webdevelopment-internship-activity-7110183314832932864-12pf?utm_source=share&utm_medium=member_desktop)

Feel free to watch the video to see the project in action and leave your comments or feedback. Your thoughts are greatly appreciated!

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

##Screenshots
- Home Page
![image](https://github.com/pyMustafa/Basic_banking_system/assets/31818881/499f3435-379d-4c33-a854-72fa7d005941)
![image](https://github.com/pyMustafa/Basic_banking_system/assets/31818881/fc83a0b9-43a6-4343-b13b-41fe35645a8e)
- All Customers
![image](https://github.com/pyMustafa/Basic_banking_system/assets/31818881/8fc9a163-e3b8-4a91-8b9b-4372ecacdf35)
- Customer Details
![image](https://github.com/pyMustafa/Basic_banking_system/assets/31818881/9b3b62b4-889e-494c-8b1a-01c887cecf65)
- Seiding Money
![image](https://github.com/pyMustafa/Basic_banking_system/assets/31818881/25a8fc55-0c46-469d-9e52-90983307db41)
- Transactions History
![image](https://github.com/pyMustafa/Basic_banking_system/assets/31818881/a1950a0f-053c-4034-980c-2f2a92af3bd3)
![image](https://github.com/pyMustafa/Basic_banking_system/assets/31818881/5947b19c-8174-427e-a27c-2c67aa4baa34)





