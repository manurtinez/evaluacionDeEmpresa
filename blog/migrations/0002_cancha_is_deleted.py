# Generated by Django 3.0.1 on 2019-12-18 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancha',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
