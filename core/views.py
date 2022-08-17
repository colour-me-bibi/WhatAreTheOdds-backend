from rest_framework.viewsets import ModelViewSet
from .models import MarketModel
from .serializers import MarketDetailSerializer, MarketSerializer


class MarketsViewSet(ModelViewSet):
    queryset = MarketModel.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return MarketSerializer

        return MarketDetailSerializer
