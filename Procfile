release: python src/manage.py migrate
web: gunicorn --pythonpath src blog.wsgi --preload --log-file -