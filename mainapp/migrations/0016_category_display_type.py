# Generated by Django 3.2.4 on 2021-09-03 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_alter_category_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='display_type',
            field=models.IntegerField(default=1),
        ),
    ]
