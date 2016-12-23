import sae
from wechat import chris_wechat
from chris_wechat import wsgi

application = sae.create_wsgi_app(wsgi.application)