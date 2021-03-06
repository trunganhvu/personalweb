from mainapp.model.Category import Category
from django.db import models

class CategoryPost(models.Model):
    """
    trunganhvu 2021/08/29
    """
    category_post_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    category_post_content = models.TextField()
    category_post_description = models.CharField(max_length=600)
    category_post_image_name = models.CharField(max_length=100)
    category_post_image = models.CharField(max_length=255)
    category_post_title = models.CharField(max_length=255)
    category_post_url = models.CharField(max_length=100)
    display = models.BooleanField(default=False)
    display_order = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        app_label = "mainapp"
