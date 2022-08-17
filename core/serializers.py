from rest_framework.serializers import ModelSerializer

from . import models as core_models


class TagSerializer(ModelSerializer):
    class Meta:
        model = core_models.Tag
        fields = "__all__"


class ContractSerializer(ModelSerializer):
    class Meta:
        model = core_models.Contract
        fields = "__all__"


class MarketDetailSerializer(ModelSerializer):
    tags = TagSerializer(many=True)
    contracts = ContractSerializer(many=True)

    class Meta:
        model = core_models.MarketModel
        fields = "__all__"


class MarketSerializer(ModelSerializer):
    class Meta:
        model = core_models.MarketModel
        fields = "__all__"
