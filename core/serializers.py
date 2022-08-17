from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User
from .models import Investment, Tag, Offer, Market, Contract, UserProfile
from dj_rest_auth.serializers import UserDetailsSerializer


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["user", "tokens"]


class UserSerializer(UserDetailsSerializer):
    # tokens = UserProfileSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ContractSerializer(ModelSerializer):
    class Meta:
        model = Contract
        fields = "__all__"


class MarketDetailSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    contracts = ContractSerializer(many=True)

    class Meta:
        model = Market
        fields = "__all__"

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        contracts = validated_data.pop('contracts')
        market = Market.objects.create(**validated_data)
        for tag in tags:
            market.tags.add(tag)
        for contract in contracts:
            market.contracts.add(contract)
        return market

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags')
        contracts = validated_data.pop('contracts')
        instance.__dict__.update(**validated_data)
        instance.save()
        instance.tags.clear()
        for tag in tags:
            instance.tags.add(tag)
        instance.contracts.clear()
        for contract in contracts:
            instance.contracts.add(contract)
        return instance


class MarketSerializer(ModelSerializer):
    class Meta:
        model = Market
        fields = "__all__"


class OfferSerializer(ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"


class InvestmentSerializer(ModelSerializer):
    class Meta:
        model = Investment
        fields = "__all__"


class PortfolioSerializer(Serializer):
    user = UserSerializer()
    offers = OfferSerializer(many=True)
    investments = InvestmentSerializer(many=True)
