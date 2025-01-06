from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from leads.views import LeadViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'leads', LeadViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # URL para acessar a documentação OpenAPI
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
