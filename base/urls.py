from django.urls import path

from .views import getRoutes, getproduits, getproduit

urlpatterns = [
    path('', getRoutes, name="routes"),
    path('produits/', getproduits, name="produits"),
    path('produits/<str:pk>/', getproduit, name="produit"),
]