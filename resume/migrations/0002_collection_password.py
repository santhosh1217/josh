# Generated by Django 4.0.6 on 2022-08-20 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='password',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
