from django.contrib import admin
from django.http import JsonResponse
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('leads.urls')),
    path('', lambda request: JsonResponse({'message': 'Welcome to the Lead Management API!'})),
]
