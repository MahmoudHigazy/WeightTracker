import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weightlifting_tracker.settings')
application = get_wsgi_application()
