import sae
from app_name import wsgi

application = sae.create_wsgi_app(wsgi.application)