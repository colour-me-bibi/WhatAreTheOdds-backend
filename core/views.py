from rest_framework.viewsets import ModelViewSet

from .models import Investment, Market, Offer
from .serializers import InvestmentSerializer, MarketDetailSerializer, MarketSerializer, OfferSerializer, PortfolioSerializer
from rest_framework.response import Response

from dj_rest_auth.serializers import UserDetailsSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


class MarketsViewSet(ModelViewSet):
    queryset = Market.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return MarketSerializer

        return MarketDetailSerializer


class OfferViewSet(ModelViewSet):
    serializer_class = OfferSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Offer.objects.filter(user=self.request.user)


class InvestmentViewSet(ModelViewSet):
    serializer_class = InvestmentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Investment.objects.filter(user=self.request.user)


class RetrievePortfolioView(RetrieveAPIView):
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user

        return Response({
            "user": UserDetailsSerializer(user).data,
            'offers': OfferSerializer(Offer.objects.filter(user=user), many=True).data,
            'investments': InvestmentSerializer(Investment.objects.filter(user=user), many=True).data
        })


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def purchase_tokens_view(request):
    # TODO set up user profile

    user = request.user
    amount = request.data.get('amount')

    if amount is None:
        return Response({"error": "amount is required"}, status=400)

    user.profile.purchase_tokens(amount)
    return Response({"message": "tokens purchased"}, status=200)
