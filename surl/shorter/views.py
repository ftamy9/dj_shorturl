from django.http import HttpResponseRedirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Address

from .serializer.AddressSerializer import AddressSerializer


@api_view(['GET', 'POST'])
def address_detail(request, id):

    if request.method == 'GET':
        # # get/redirect

        try:
            address = Address.objects.get(id=id)
        except (Address.DoesNotExist, ValueError):
            return Response({'error': 'No item found matching the url'}, status=status.HTTP_406_NOT_ACCEPTABLE)

        # return HttpResponseRedirect(redirect_to=f'http://{address.url}')
        return HttpResponseRedirect(redirect_to=address.url)

    elif request.method == 'POST':
        # create
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
            except Exception as e:
                return Response({'error': str(e)}, status= status.HTTP_409_CONFLICT)

            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


    #TODO: delete url