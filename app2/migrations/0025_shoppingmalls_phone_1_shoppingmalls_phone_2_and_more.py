# Generated by Django 4.0.1 on 2022-01-26 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0024_shoppingmalls_gmail_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingmalls',
            name='phone_1',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shoppingmalls',
            name='phone_2',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shoppingmalls',
            name='phone_3',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='shoppingmalls',
            name='phone_4',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
