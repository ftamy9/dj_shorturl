from rest_framework import status, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from small_auth.serializers.BaseUserSerializer import UserSerializer
from small_auth.models import BaseUser
from small_auth.simple_sign import create_sing, create_token

from django.conf import settings


@api_view(['POST', 'PUT'])
@authentication_classes([])
@permission_classes([]) #permission_classes  = ()
def user_detail(request):

    if request.method == 'POST':
        # create
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({'error': str(e)}, status= status.HTTP_409_CONFLICT)

            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        # login

        try:
            raw_password = request.data['password_hash']
            user = BaseUser.objects.get(
                id=request.data['id'],
                password_hash=create_sing(raw_password.encode(), settings.PASSWORD_SECRET)
            )

        except Exception as e:
            return Response({'errors': str(e)}, status=status.HTTP_406_NOT_ACCEPTABLE)

        return Response({'toke': create_token(user.id)}, status=status.HTTP_200_OK)

    #TODO: password change