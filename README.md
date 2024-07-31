# Medical Appointment and Blog Website

This is a Django-based web application that allows users to book medical appointments, read and comment on blog posts, and send contact messages. It also includes administrative features for managing appointments, blog posts, and website content.

## Features

### User Authentication
- Users can register and log in.
- Authentication system that supports three user roles: common users, administrative users, and staff users.

### Medical Appointments
- Users can book medical appointments by providing their name, email, phone number, department (e.g., Neurology, Dentistry), and additional information.
- Administrative users can view and manage all appointments.

### Blog
- Administrative users can publish blog posts.
- Common users can read and comment on blog posts.

### Contact Form
- Users can send messages through a contact form on the website.
- Messages are sent to a designated email address.

### Administrative Users
- Can view all appointments booked by patients.
- Can publish blog posts and showcase clinic portfolio appointments.

### Staff Users
- Can do everything administrative users can do.
- Can update any information on the website, allowing them to correct errors or make updates without needing to hire developers.

## Getting Started

### Installation
1. Clone the repository:
   ```sh
   git clone 
   cd medical-appointment-blog-website
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:
 ```sh
   pip install django
   pip install djangorestframework
```

Set up the database:
```sh
   python manage.py makemigrations
   python manage.py migrate
```
Create a superuser:
```sh
   python manage.py createsuperuser
```

Run the development server:
```sh
python manage.py runserver
```
Open your browser and navigate to http://localhost:8000 to view the website.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

