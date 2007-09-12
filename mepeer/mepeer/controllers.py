import logging

import cherrypy

import turbogears
from turbogears import controllers, expose, validate, redirect

from mepeer import json

log = logging.getLogger("mepeer.controllers")

class Root(controllers.RootController):
    @expose(template="mepeer.templates.welcome")
    def index(self):
        import time
        log.debug("Happy TurboGears Controller Responding For Duty")
        return dict(now=time.ctime())
