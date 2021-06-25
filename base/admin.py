from django.contrib import admin
from .models import Produit, AddLivraison, CmdeItem, Commande, Commentaire

admin.site.register(Produit)
admin.site.register(AddLivraison)
admin.site.register(CmdeItem)
admin.site.register(Commande)
admin.site.register(Commentaire)

# Register your models here.
