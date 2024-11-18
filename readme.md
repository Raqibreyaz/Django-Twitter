#  Django Twitter-like CRUD App

[![Django](https://img.shields.io/badge/Django-4.x-brightgreen)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/Database-SQLite3-blue)](https://www.sqlite.org/index.html)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📌 Overview

This is a Full Stack Twitter-like CRUD application built using **Django**, **Jinja2** templating engine, and **SQLite3** as the database. The app allows users to register, log in, and manage their posts (Create, Read, Update, Delete). It utilizes Django's built-in **User Model** for authentication and Django Forms for handling user input.

## 🚀 Tech Stack

- **Frontend**: HTML, CSS, Jinja2 (Django Templating Engine)
- **Backend**: Python, Django
- **Database**: SQLite3

## 🎯 Features

- User registration and login using Django's built-in User model
- Create, read, update, and delete (CRUD) posts
- User authentication and session management
- Responsive UI using Django's template system with Jinja2                    |

## 🛠️ Setup and Installation

To set up the project locally, follow these steps:

- Ensure Python is installed (version 3.7+ recommended)

### 1. Install UV if its not already installed
    pip install uv

### 2. Create a virtual environment using UV
    uv venv .venv

### 3. Activate the virtual environment
- For Windows
    ```bash
    .venv\Scripts\activate

- For MacOS/Linux
    ```bash
    source .venv/bin/activate

### 4. Install the required dependencies from requirements.txt
    pip install -r requirements.txt

### 5. Run database migrations to set up the SQLite database
    python manage.py migrate

### 6. Optionally, create a superuser for accessing the Django admin panel
    python manage.py createsuperuser

### 7. Start the Django development server
    python manage.py runserver
