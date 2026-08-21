import os
import socket
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "microsite.settings")

# if socket.gethostbyname(socket.gethostname()) == "136.243.86.126":
#     import newrelic.agent

application = get_wsgi_application()

# Alias for Vercel WSGI resolution
app = application