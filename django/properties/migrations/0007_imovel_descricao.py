# Generated by Django 3.1.3 on 2020-12-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0006_auto_20201222_1314'),
    ]

    operations = [
        migrations.AddField(
            model_name='imovel',
            name='descricao',
            field=models.TextField(blank=True, null=True),
        ),
    ]
