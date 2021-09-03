from mainapp.model.CategoryPost import CategoryPost
from mainapp.model.Category import Category
from django.conf import settings
from django.conf.urls import url
from django.shortcuts import render
from django.shortcuts import redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from mainapp.service.Category import CategoryService, CategoryPostService
from django.utils.safestring import mark_safe
from django.contrib import messages
from mainapp.Common import ConstValiable

import re, os

def view_insert_category_post_page(request, category_id):
    """
    View page insert post
    """
    context = {}
    try:
        category = CategoryService.get_category_detail(category_id)
        context = {
            'category': category
        }
        
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/category')
    return render(request, 'private/Category/categorypostform.html', context)

def view_update_category_post_page(request, category_id, post_id):
    """
    View page insert post
    """
    context = {}
    try:
        print('form update')
        category = CategoryService.get_category_detail(category_id)
        post = CategoryPostService.get_detail_post_by_id(post_id)
        context = {
            'category': category,
            'category_post': post
        }
        print('query done')
    except Exception as error:
        print(error)
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/category')
    return render(request, 'private/Category/categorypostform.html', context)
    
def insert_category_post_form(request, category_id):
    """
    Insert new post
    """
    if request.method == 'POST':
        try:
            print('123 post')
            # Get data in form
            category_post_title = request.POST.get('category-post-title')
            category_post_url = request.POST.get('category-post-url')
            category_post_description = request.POST.get('category-post-description')
            category_post_content = request.POST.get('category-post-content')
            category_post_image_name = request.POST.get('category-post-image-name')
            
            category_post_image = request.FILES['category-post-image']
            category_post_display = request.POST.get('category-post-display')
            category_post_display_order = request.POST.get('category-post-display-order')
            print('view 1')
            category_post = CategoryPost(category_id=category_id,
                                category_post_title=category_post_title,
                                category_post_url=category_post_url,
                                category_post_description=category_post_description,
                                category_post_content=category_post_content,
                                category_post_image_name=category_post_image_name,
                                category_post_image=category_post_image,
                                display=category_post_display,
                                display_order=category_post_display_order)
            context = {
                'category_post': category_post
            }
            print('view 2')
            is_update_image = True
            check = validate_form(category_post, is_update_image)
            if check:
                CategoryPostService.insert_post(category_post)
                messages.success(request, ConstValiable.MESSAGE_POPUP_SUCCESS)
            else:
                messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
                return render(request, 'private/Category/categoryform.html', context=context)

        except Exception:
            messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
            return render(request, 'private/Category/categoryform.html')
    return redirect('/category/' + category_id)

def update_category_post_form(request, category_id, post_id):
    """
    Update post
    """
    print(category_id, post_id)
    return render(request, 'private/Category/categorypostform.html')

def view_category_post_detail_page(request, category_id, post_id):
    """
    View detail post by id
    """
    try:
        category = CategoryService.get_category_detail(category_id)
        post = CategoryPostService.get_detail_post_by_id(post_id)
        context = {
            'category': category,
            'category_post': post
        }
        return render(request, 'private/Category/categorypostdetail.html', context)
    except Exception:
        messages.error(request, ConstValiable.MESSAGE_POPUP_ERROR)
        return redirect('/category')

def validate_form(category_post, is_update_image):
    """
    Validate data form insert category
    """
    re_name = "^[A-Za-z0-9_ ]*$"
    re_url = "^[A-Za-z0-9_-]*$"
    # Check title
    if category_post.category_post_title is None or not re.match(re_name, category_post.category_post_title):
        return False
    # Check url
    if category_post.category_post_url is None or not re.match(re_url, category_post.category_post_url):
        return False
    # Check content
    if category_post.category_post_content is None or not re.match(re_url, category_post.category_post_content):
        return False
    # Check des
    if category_post.category_post_description is None or not re.match(re_url, category_post.category_post_description):
        return False
    # Check image name
    if category_post.category_post_image_name is None or not re.match(re_url, category_post.category_post_image_name):
        return False
    # Check image type
    if is_update_image:
        image_split = category_post.category_post_image.name.split('.')
        image_type = image_split[-1]
        check = image_type in ['png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif', 'webp']
        if not check:
            return False
    # Check display
    if not category_post.display in ['true', 'false']:
        return False
    if category_post.display == 'true':
        if not category_post.display_order.isnumeric() or int(category_post.display_order) <= 0:
            return False
    return True