
from django.contrib import admin

from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView
from rest_framework import routers

from .views import (InvestmentViewSet, MarketsViewSet, OfferViewSet,
                    RetrievePortfolioView, purchase_tokens_view)

router = routers.DefaultRouter()
router.register(r"markets", MarketsViewSet)
router.register(r"offers", OfferViewSet, basename="offers")
router.register(r"investments", InvestmentViewSet, basename="investments")

urlpatterns = [
    path('', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    path("admin/", admin.site.urls),

    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    path('', include(router.urls)),

    path("portfolio/", RetrievePortfolioView.as_view(), name="portfolio"),
    path('purchase_tokens/', purchase_tokens_view, name='purchase_tokens'),
]
