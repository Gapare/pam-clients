import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pam_estates.settings')

app = get_wsgi_application()

# Vercel needs this
application = app