# Generated by Django 3.2.4 on 2021-08-31 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_header_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='header',
            name='image_event_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='header',
            name='image_event_path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
