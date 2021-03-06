# Generated by Django 3.1.3 on 2020-12-14 13:16

from django.db import migrations, models
import django.db.models.deletion
import gdstorage.storage


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0004_auto_20201214_1316'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30, verbose_name='Nome')),
                ('file', models.ImageField(storage=gdstorage.storage.GoogleDriveStorage(), upload_to='fotos')),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='properties.imovel')),
            ],
            options={
                'verbose_name': 'Foto',
                'verbose_name_plural': 'Foto',
            },
        ),
    ]
