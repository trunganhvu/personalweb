# Generated by Django 3.2.4 on 2021-09-11 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_alter_categorypost_category_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcolor',
            name='product_type_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mainapp.producttype'),
            preserve_default=False,
        ),
    ]
