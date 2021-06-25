from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import produits
from .models import Produit
from .serailizers import ProduitSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/produits/',
        '/api/produits/add/',

        '/api/produits/upload/',

        '/api/produits/<id>/reviews',

        '/api/produits/top/',
        '/api/produits/<id>/',

        '/api/produits/delete/<id>/',
        '/api/produits/update/<id>/',

    ]
    return Response(routes)

@api_view(['GET'])
def getproduits(request):
    produits = Produit.objects.all().order_by('-ajouter_le')
    serializer = ProduitSerializer(produits, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getproduit(request, pk):
    produit = Produit.objects.get(_id=pk)
    serializer = ProduitSerializer(produit, many=False)
    return Response(serializer.data)

# Create your views here.
