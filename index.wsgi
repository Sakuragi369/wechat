#coding:utf-8 
import sys
import os.path

os.environ['DJANGO_SETTINGS_MODULE'] = 'wechat.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'wechat'))

import sae
from wechat import wsgi

application = sae.create_wsgi_app(wsgi.application)