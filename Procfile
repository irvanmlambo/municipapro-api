release: python manage.py migrate
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker plane.asgi:application --bind 0.0.0.0:$PORT --config gunicorn.config.py --max-requests 10000 --max-requests-jitter 1000 --access-logfile -
worker: celery -A plane worker -l info
beat: celery -A plane beat -l INFO