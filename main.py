import webapp2
from webapp2_extras.routes import RedirectRoute


routes = [
    RedirectRoute('/', redirect_to='/engineauth/index.html'),
    RedirectRoute('/engineauth', redirect_to='/engineauth/index.html'),
]

application = webapp2.WSGIApplication(routes)
