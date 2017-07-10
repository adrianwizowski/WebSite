from django.utils.deprecation import MiddlewareMixin
from django_user_agents.middleware import UserAgentMiddleware

'''Custom middleware passes args to  Django User Agent.
User Agent doesn't work with with Django 1.10 without custom middleware...'''

class CustomUserAgentMiddleware(MiddlewareMixin, UserAgentMiddleware):
    pass