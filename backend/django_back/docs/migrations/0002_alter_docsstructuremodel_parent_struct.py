# Generated by Django 4.2.4 on 2023-09-04 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsstructuremodel',
            name='parent_struct',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='parent', to='docs.docsstructuremodel'),
        ),
    ]
