from rest_framework.serializers import ModelSerializer, Serializer, PrimaryKeyRelatedField, ManyRelatedField, RelatedField
from django.contrib.auth.models import User
from .models import Investment, Tag, Offer, Market, Contract, UserProfile
from dj_rest_auth.serializers import UserDetailsSerializer


# class ProfileSerializer(ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = "__all__"


class UserSerializer(UserDetailsSerializer):
    # profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user


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
            Tag.objects.create(market=market, **tag)

        for contract in contracts:
            Contract.objects.create(market=market, **contract)

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
