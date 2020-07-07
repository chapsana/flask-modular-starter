# Flask Dashboard Modular

<br />

## Dashboard Features:

- UI-Ready, SQLite database
- SQLAlchemy ORM
- Session-Based authentication flow (login, register)
- Forms validation
- UI Kit: **[ModularCode](https://modularcode.io/?ref=appseed)**

<br />

## Build from sources

```bash
# Clone the sources

# Virtualenv modules installation (Unix based systems) --no-site-packages
virtualenv  env
source env/bin/activate

# Virtualenv modules installation (Windows based systems)
# virtualenv --no-site-packages env
# .\env\Scripts\activate.bat

# Install requirements
pip3 install -r requirements.txt

# Set the FLASK_APP environment variable
# (Unix/Mac) export FLASK_APP=run.py
# (Windows) set FLASK_APP=run.py
# (Powershell) $env:FLASK_APP = ".\run.py"

# Set up the DEBUG environment
# (Unix/Mac) export FLASK_ENV=development
# (Windows) set FLASK_ENV=development
# (Powershell) $env:FLASK_ENV = "development"

# Run the application
# --host=0.0.0.0 - expose the app on all network interfaces (default 127.0.0.1)
# --port=5000    - specify the app port (default 5000)
flask run --host=0.0.0.0 --port=5000

# Access the app in browser: http://127.0.0.1:5000/
```

<br />

## Deployment

The app is provided with a basic configuration to be executed in [Docker](https://www.docker.com/), [Gunicorn](https://gunicorn.org/), and [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/).

<br />

### [Docker](https://www.docker.com/) execution

---

The application can be easily executed in a docker container. The steps:

> Get the code

```bash
cd flask-dashboard-modular
```

> Start the app in Docker

```bash
sudo docker-compose pull && sudo docker-compose build && sudo docker-compose up -d
```

Visit `http://localhost:5005` in your browser. The app should be up & running.

<br />

### [Gunicorn](https://gunicorn.org/)

---

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX.

> Install using pip

```bash
pip install gunicorn
```

> Start the app using gunicorn binary

```bash
gunicorn --bind 0.0.0.0:8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

### [Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/)

---

Waitress (Gunicorn equivalent for Windows) is meant to be a production-quality pure-Python WSGI server with very acceptable performance. It has no dependencies except ones that live in the Python standard library.

> Install using pip

```bash
pip install waitress
```

> Start the app using [waitress-serve](https://docs.pylonsproject.org/projects/waitress/en/stable/runner.html)

```bash
waitress-serve --port=8001 run:app
Serving on http://localhost:8001
```

Visit `http://localhost:8001` in your browser. The app should be up & running.

<br />

## Credits & Links

- [Flask Framework](https://www.palletsprojects.com/p/flask/)
- [Modular Admin](https://github.com/modularcode/modular-admin-html)
