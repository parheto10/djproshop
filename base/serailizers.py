from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Produit, AddLivraison, CmdeItem, Commande, Commentaire


class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'
