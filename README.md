# Calorie Counter – Django Web Application

A simple calorie tracking web app built with Django, PostgreSQL, and Tailwind CSS. Users can add, view, delete food items, see the total daily calorie intake, and reset the day’s entries.

---

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Local Development Setup](#local-development-setup)
- [Environment Variables](#environment-variables)
- [Database Configuration](#database-configuration)
- [Running the Application](#running-the-application)
- [Deployment to Render](#deployment-to-render)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- **Add food items** with name and calorie count.
- **View list** of all items logged today.
- **Remove** any item from the list.
- **Calculate total calories** for the day.
- **Reset** all today's entries with a confirmation prompt.
- **Responsive design** using Tailwind CSS.
- **User-friendly messages** (success, info, warning) using Django's messages framework.

---

## Technologies Used

- **Backend:** Django 4.2 (Python 3.10+)
- **Database:** PostgreSQL (local and production)
- **Frontend:** HTML5, Tailwind CSS (CDN)
- **Deployment:** Render (PaaS) with Gunicorn

---

## Project Structure

```text
calorie-counter/
├── manage.py
├── calorie_counter/           # project settings package
│   ├── __init__.py
│   ├── settings.py            # Django settings (local + production)
│   ├── urls.py                # root URL config
│   └── wsgi.py                # WSGI entry point
├── calorie_tracker/           # main app
│   ├── __init__.py
│   ├── admin.py               # admin registration
│   ├── apps.py
│   ├── models.py              # FoodItem model
│   ├── views.py               # index, delete, reset views
│   ├── forms.py               # FoodItemForm
│   ├── urls.py                # app URL patterns with namespace
│   ├── migrations/
│   │   └── 0001_initial.py
│   └── templates/
│       └── calorie_tracker/
│           ├── base.html
│           └── index.html
├── requirements.txt
├── runtime.txt
├── Procfile
├── .gitignore
└── README.md
```

---

## Local Development Setup

### Prerequisites

- Python 3.10 or higher installed
- PostgreSQL installed and running (or you can switch to SQLite)
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Kyle-00/calorie-counter-1.git
cd calorie-counter
```

### 2. Create and activate a virtual environment

**Windows (Git Bash):**

```bash
python -m venv venv
source venv/Scripts/activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure PostgreSQL (local)

Make sure PostgreSQL is running and you have created a database and user:

```sql
CREATE DATABASE calorie_db;
CREATE USER calorie_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE calorie_db TO calorie_user;
```

In `calorie_counter/settings.py`, update the `DATABASES` section (or use environment variables).
The default local configuration uses:

- **NAME:** `calorie_db`
- **USER:** `calorie_user`
- **PASSWORD:** set via your local environment (do not commit real credentials)
- **PORT:** `5433`

### 5. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## Environment Variables

For production, you must set the following environment variables (e.g., on Render):

| Variable | Description | Example |
| --- | --- | --- |
| `SECRET_KEY` | Django secret key | `django-insecure-...` (generate a strong one) |
| `DEBUG` | Set to `False` | `False` |
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host:port/db` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `your-app.onrender.com` (or `*` for development) |

For local development, the settings default to the PostgreSQL config (port 5433) and a fallback secret key — never use the fallback in production.

---

## Database Configuration

The `settings.py` file uses conditional logic:

- If `DEBUG` is `True` (local), it uses the hard-coded PostgreSQL connection (port 5433, user `calorie_user`). You can change these values in the file or switch to SQLite.
- If `DEBUG` is `False` (production), it reads the `DATABASE_URL` environment variable via `dj_database_url`.

---

## Running the Application

After setting up the database and applying migrations, start the server:

```bash
python manage.py runserver
```

The app will be available at `http://127.0.0.1:8000/`.

---

## Deployment to Render

### Step 1 – Push code to GitHub

Make sure your repository is up to date:

```bash
git add .
git commit -m "Finalize project for deployment"
git push origin main
```

### Step 2 – Create a PostgreSQL database on Render

1. Log in to Render.
2. Go to the Dashboard and click **New +** → **PostgreSQL**.
3. Fill in the details (name, region, etc.) and create the database.
4. Once created, copy the **Internal Database URL** (this will be used as `DATABASE_URL`).

### Step 3 – Create a Web Service

1. On Render Dashboard, click **New +** → **Web Service**.
2. Connect your GitHub repository.
3. Fill in the following (view the table below):

| Field | Value |
| --- | --- |
| Name | `calorie-counter` (or any name) |
| Environment | Python |
| Build Command | `pip install -r requirements.txt && python manage.py collectstatic --noinput` |
| Start Command | `gunicorn calorie_counter.wsgi` |
| Python Version | 3.10 (or the version you set in `runtime.txt`) |

4.Under **Environment Variables**, add:

- `DATABASE_URL` → paste the Internal Database URL from your Render PostgreSQL.
- `SECRET_KEY` → generate a random key (e.g., using Django's `from django.core.management.utils import get_random_secret_key`).
- `DEBUG` → `False`
- `ALLOWED_HOSTS` → `your-app-name.onrender.com` (or leave as `*` temporarily)

5.Click **Create Web Service**.

Render will build and deploy your app. Once finished, you will receive a live URL like `https://calorie-counter.onrender.com`.

---

## Contributing

This is a personal project, but if you find any issues or have suggestions, feel free to open an issue or submit a pull request.

---

## License

Licensed by MIT.
