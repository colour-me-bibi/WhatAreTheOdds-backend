

from django.urls import path
from drf_spectacular.views import SpectacularRedocView

urlpatterns = [
    path('docs/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
