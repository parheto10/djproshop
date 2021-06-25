from django.contrib.auth.models import User
from django.db import models

class Produit(models.Model):
    _id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey(User ,on_delete=models.SET_NULL, null=True)
    nom = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='%m/%Y')
    marque = models.CharField(max_length=255, null=True, blank=True)
    categorie = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    notation = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    nb_commentaire = models.IntegerField(null=True, blank=True, default=0)
    prix = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    stock = models.IntegerField(null=True, blank=True, default=0)
    ajouter_le = models.DateTimeField(auto_now_add=True)
    update_le = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' %(self.nom)

class Commentaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    nom  = models.CharField(max_length=255, null=True, blank=True)
    notation = models.IntegerField(default=0, null=True, blank=True)
    commentaire = models.TextField(null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return '%s' %(self.notation)

class Commande(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mode_paiement = models.CharField(max_length=255, null=True, blank=True)
    taxe = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    transport = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    is_paye = models.BooleanField(default=False)
    paye_le = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    is_delivre = models.BooleanField(default=False)
    delivre_le = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    ajouter_le = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return '%s' %(self.ajouter_le)

class CmdeItem(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    nom= models.CharField(max_length=255, blank=True, null=True)
    qty = models.IntegerField(default=0, null=True, blank=True)
    prix = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.CharField(max_length=255, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return '%s' %(self.nom)

class AddLivraison(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE, null=True, blank=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    ville = models.CharField(max_length=255, blank=True, null=True)
    quartier = models.CharField(max_length=255, blank=True, null=True)
    code_postale = models.CharField(max_length=255, blank=True, null=True)
    pays = models.CharField(max_length=255, blank=True, null=True)
    prix_livraison = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return '%s' % (self.adresse)







# Create your models here.
