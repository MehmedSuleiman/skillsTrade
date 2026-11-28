from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from skillsTrade import settings

class RequestCountMiddleware(MiddlewareMixin):
    SESSION_KEY = 'limit_logs'
    window_seconds = 60

    def process_request(self, request):
        _now = now().timestamp()
        window_start = _now - self.window_seconds

        recent_requests = [
            t for t in request.session.get(self.SESSION_KEY, [])
            if t > window_start
        ]

        if len(recent_requests) >= settings.REQUESTS_PER_MINUTE:
            return HttpResponse("Too many requests!", status=429)

        recent_requests.append(_now)
        request.session[self.SESSION_KEY] = recent_requests