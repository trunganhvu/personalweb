# Generated by Django 3.2.4 on 2021-09-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20210903_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorypost',
            name='category_post_image_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
