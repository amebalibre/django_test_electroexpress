"""URL Main Configuration."""
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    path('ecommerce/', include('ecommerce.urls')),
    path('admin/', admin.site.urls),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', include_docs_urls(title='Django Test Electroexpress API')),
]
