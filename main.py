#!/usr/bin/env python
import os
import webapp2

from google.appengine.ext.webapp import template
from webapp2_extras import routes



class MainHandler(webapp2.RequestHandler):
    def get(self):
        # self.response.write('Coming soon!')

        path = os.path.join(os.path.dirname(__file__), 'template/coming_soon.html')
        params = {}
        self.response.out.write(template.render(path, params))


class PreviewHandler(webapp2.RequestHandler):
    def get(self):

        path = os.path.join(os.path.dirname(__file__), 'template/index.html')
        params = {}
        self.response.out.write(template.render(path, params))



app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:(gammafund.org|localhost)>', [
        webapp2.Route('/', MainHandler),
    ]),

    ('/', PreviewHandler)
])
