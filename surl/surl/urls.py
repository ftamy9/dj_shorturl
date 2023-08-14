from django.contrib import admin
from django.urls import path

from shorter.views import address_detail
from small_auth.views import user_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/signup', user_detail),
    path('shorter/url/<uuid:id>',  address_detail),
    path('shorter/url', address_detail, kwargs={'id': None}),
]
