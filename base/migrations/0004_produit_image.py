# Generated by Django 3.1.7 on 2021-06-24 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_addlivraison_cmdeitem_commande_commentaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='%m/%Y'),
        ),
    ]