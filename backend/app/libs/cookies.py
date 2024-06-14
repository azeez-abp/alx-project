from flask import Flask  # type: ignore
from datetime import datetime, timedelta, timezone

app = Flask(__name__)


class CookieHandler:
    @staticmethod
    def set_cookie(response, name, value, max_age, secure=True, httponly=True,
                   samesite='Lax'):
        expires = datetime.now(timezone.utc) + timedelta(seconds=max_age)
        response.set_cookie(name, value, expires=expires, secure=secure,
                            httponly=httponly, samesite=samesite)

    @staticmethod
    def get_cookie(request, name):
        return request.cookies.get(name)
