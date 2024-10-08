# Generated by Django 5.1.1 on 2024-10-08 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_carro_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='ano',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carro',
            name='placa',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sobrenome',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
