from django.urls import path, include
from drf_spectacular.views import SpectacularRedocView, SpectacularAPIView
from rest_framework import routers

from . import views as core_views


router = routers.DefaultRouter()
router.register(r"markets", core_views.MarketsViewSet)

urlpatterns = [
    path('', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    path('', include(router.urls)),
]
