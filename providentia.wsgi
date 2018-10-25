#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/Providentia/Providentia/")

from Providentia import app as application
application.secret_key = 'surveillance'
