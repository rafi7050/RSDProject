# Generated by Django 3.1.7 on 2021-02-23 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0013_auto_20210222_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to=None, verbose_name='Product Image'),
        ),
    ]
