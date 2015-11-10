import sys
import os.path
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
sys.path.append(os.path.join(os.path.dirname(__file__), 'mysite'))

import sae
from mysite import wsgi

application = sae.create_wsgi_app(wsgi.application)