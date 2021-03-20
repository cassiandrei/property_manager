# Generated by Django 3.1.3 on 2020-12-22 13:14

from django.db import migrations, models
import gdstorage.storage


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foto',
            name='file',
            field=models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='fotos', verbose_name='Arquivo'),
        ),
        migrations.AlterField(
            model_name='foto',
            name='nome',
            field=models.CharField(max_length=300, verbose_name='Nome'),
        ),
    ]