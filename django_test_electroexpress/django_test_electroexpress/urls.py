"""URL Main Configuration."""
from django.contrib import admin
from django.urls import path
# from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    path('ecommerce/', include('ecommerce.urls')),
    path('admin/', admin.site.urls),
    # url(r'^api-auth/',
    #     include('rest_framework.urls', namespace='rest_framework'))
]
