# Generated by Django 4.0.1 on 2022-01-26 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app2', '0013_shoppingmalls_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shoppingmalls',
            old_name='demo_link',
            new_name='facebook_link',
        ),
        migrations.RenameField(
            model_name='shoppingmalls',
            old_name='source_link',
            new_name='other_link',
        ),
        migrations.AddField(
            model_name='shoppingmalls',
            name='website_link',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
