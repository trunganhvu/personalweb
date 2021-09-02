# Generated by Django 3.2.4 on 2021-09-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_auto_20210901_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title', models.CharField(max_length=60)),
                ('banner_subtitle', models.CharField(max_length=120)),
                ('display', models.BooleanField(default=False)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]