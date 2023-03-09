# Generated by Django 4.1.7 on 2023-03-09 19:09

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_thumbnailsize_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thumbnailsize',
            name='height',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='tier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='core.accounttier'),
        ),
    ]
