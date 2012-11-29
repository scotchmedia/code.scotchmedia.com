import webapp2
from webapp2_extras.routes import RedirectRoute


routes = [
    RedirectRoute('/', redirect_to='/engineauth/docs/index.html'),
    RedirectRoute('/engineauth', redirect_to='/engineauth/docs/index.html'),
    RedirectRoute('/engineauth/', redirect_to='/engineauth/docs/index.html'),
    RedirectRoute('/engineauth/docs', redirect_to='/engineauth/docs/index.html'),
    RedirectRoute('/engineauth/docs/', redirect_to='/engineauth/docs/index.html'),
]

application = webapp2.WSGIApplication(routes)
