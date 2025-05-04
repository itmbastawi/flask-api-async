# flask-api-async
Flask async API 

my_flask_api/
│
├── .env
├── .gitignore
├── requirements.txt
├── config.py
├── run.py
│
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── other_models.py
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── api.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py
│   │   └── other_schemas.py
│   │
│   └── services/
│       ├── __init__.py
│       ├── auth.py
│       └── other_services.py




# Initialize migrations
flask db init

# Create a migration
flask db migrate -m "Initial migration"

# Apply migration
flask db upgrade