import os

os.system("python manage.py migrate")
os.system("guicorn AreteLending.wsgi:application --error-logfile - --access-logfile - --bind 0.0.0.0:8000 --timeout=1000 --workers 3")
