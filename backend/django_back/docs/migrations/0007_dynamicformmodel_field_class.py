# Generated by Django 4.2.4 on 2023-09-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0006_dynamicformmodel_docsformlinkmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicformmodel',
            name='field_class',
            field=models.CharField(max_length=40, null=True),
        ),
    ]