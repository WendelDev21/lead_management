from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('leads.urls')),  # Rotas da API
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Documentação na raiz
    path('schema/', SpectacularAPIView.as_view(), name='schema'),  # Esquema OpenAPI
]
