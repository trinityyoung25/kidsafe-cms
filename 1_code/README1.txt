KidSafe Content Management System

This folder contains the source code for the KidSafe CMS web application.

System Requirements
• Python 3.10 or newer
• Django Framework
• PostgreSQL database

How to Run the System

1. Install required packages

pip install django psycopg2

2. Run database migrations

python manage.py makemigrations
python manage.py migrate

3. Create admin user

python manage.py createsuperuser

4. Start the development server

python manage.py runserver

5. Open browser and go to:

http://127.0.0.1:8000
