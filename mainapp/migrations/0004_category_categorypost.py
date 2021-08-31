# Generated by Django 3.2.4 on 2021-08-29 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_header'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=100)),
                ('category_url', models.CharField(max_length=100)),
                ('display', models.BooleanField(default=False)),
                ('display_order', models.IntegerField(default=0)),
                ('category_image_default_name', models.CharField(max_length=100)),
                ('category_image_default', models.CharField(max_length=255)),
                ('category_image_event_name', models.CharField(max_length=100)),
                ('category_image_event', models.CharField(max_length=255)),
                ('category_image_event_start', models.DateField(null=True)),
                ('category_image_event_end', models.DateField(null=True)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryPost',
            fields=[
                ('category_post_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_post_content', models.CharField(max_length=1000)),
                ('category_post_description', models.CharField(max_length=600)),
                ('category_post_image', models.CharField(max_length=255)),
                ('category_post_title', models.CharField(max_length=255)),
                ('category_post_url', models.CharField(max_length=100)),
                ('display', models.BooleanField(default=False)),
                ('display_order', models.IntegerField(default=0)),
                ('created_at', models.DateField()),
                ('updated_at', models.DateField(null=True)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category')),
            ],
        ),
    ]