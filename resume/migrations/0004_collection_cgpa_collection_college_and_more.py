# Generated by Django 4.0.6 on 2022-08-20 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_collection_language_collection_project_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='cgpa',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='college',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collection',
            name='passout',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]