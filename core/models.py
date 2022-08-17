from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Market(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rules = models.TextField()
    tags = models.ManyToManyField(Tag)
    projected_end = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    name = models.CharField(max_length=100, unique=True)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    # integer from 1 to 99
    latest_yes_price = models.IntegerField(null=True, default=50)
    latest_price_movement = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name


class Offer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    YES = "Y"
    NO = "N"
    CONTRACT_TYPE_CHOICES = (
        (YES, "Yes"),
        (NO, "No"),
    )
    contract_type = models.CharField(max_length=1, choices=CONTRACT_TYPE_CHOICES)

    BUY = "B"
    SELL = "S"
    OFFER_TYPE_CHOICES = (
        (BUY, "Buy"),
        (SELL, "Sell"),
    )
    offer_type = models.CharField(max_length=1, choices=OFFER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.contract.name} - {self.price}"


class Investment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    YES = "Y"
    NO = "N"
    CONTRACT_TYPE_CHOICES = (
        (YES, "Yes"),
        (NO, "No"),
    )
    contract_type = models.CharField(max_length=1, choices=CONTRACT_TYPE_CHOICES)

    BUY = "B"
    SELL = "S"
    OFFER_TYPE_CHOICES = (
        (BUY, "Buy"),
        (SELL, "Sell"),
    )
    offer_type = models.CharField(max_length=1, choices=OFFER_TYPE_CHOICES)

    def __str__(self):
        return f"{self.contract.name} - {self.price}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tokens = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
