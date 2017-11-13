#!/usr/bin/env python
import os
import webapp2

from google.appengine.ext.webapp import template
from webapp2_extras import routes



class IndexView(webapp2.RequestHandler):
    def get(self):

        path = os.path.join(os.path.dirname(__file__), 'template/index.html')
        params = {
            'current_page': 'home'
        }
        self.response.out.write(template.render(path, params))


class InitiativeView(webapp2.RequestHandler):
    def get(self):

        path = os.path.join(os.path.dirname(__file__), 'template/initiative.html')
        params = {
            'current_page': 'initiative'
        }
        self.response.out.write(template.render(path, params))


class StrategyView(webapp2.RequestHandler):
    def get(self):

        path = os.path.join(os.path.dirname(__file__), 'template/strategy.html')
        params = {
            'current_page': 'strategy'
        }
        self.response.out.write(template.render(path, params))


class OurTeamView(webapp2.RequestHandler):
    def get(self):

        path = os.path.join(os.path.dirname(__file__), 'template/our-team.html')
        params = {
            'current_page': 'our-team'
        }
        self.response.out.write(template.render(path, params))


class PreviewView(webapp2.RequestHandler):
    def get(self):
        return self.redirect("https://www.gammafund.org")



app = webapp2.WSGIApplication([
    routes.DomainRoute(r'<:(gammafund.org|www.gammafund.org|localhost)>', [
        webapp2.Route('/', IndexView),
        webapp2.Route('/initiative', InitiativeView),
        webapp2.Route('/strategy', StrategyView),
        webapp2.Route('/our-team', OurTeamView),
    ]),

    ('/', PreviewView)
])
