# Generated by Django 4.0.3 on 2022-08-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_oppkg_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oppkg',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
