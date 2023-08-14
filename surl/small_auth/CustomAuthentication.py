# from django.contrib.auth.models import User

from rest_framework import authentication
from rest_framework import exceptions
from .models import BaseUser
from .simple_sign import verify_token

class Authentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        succeed, username = None, None

        authorization = request.headers.get('Authorization') # get token

        try:
            succeed, username = verify_token(authorization.split()[-1])

        except Exception:
            raise exceptions.AuthenticationFailed('Token format invalid')

        if not succeed:
            raise exceptions.AuthenticationFailed(f'Token error {username}')

        try:
            user = BaseUser.objects.get(id=username) # get the user
        except BaseUser.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user') # raise exception if user does not exist

        return (user, None) # authentication successful