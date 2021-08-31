from mainapp.dao.Header import HeaderDao
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import imghdr
from django.core.cache import cache

def get_path_header():
    header = HeaderDao.get_path_header()
    context = {
        'name': header.image_default_name,
        'path': header.image_default_path
    }
    return context

def insert_header_image(header_image, header_name):
    try:
        # Set image name saved
        header_name_save = header_name + '.' + str(imghdr.what(header_image))
        # Dir save
        fs = FileSystemStorage(location=settings.IMAGE_USER)
        # Save image
        filename = fs.save(header_name_save, header_image)
        # Url dir save
        uploaded_file_url = fs.url(filename)
        full_path_image = settings.IMAGE_PATH_STATIC + uploaded_file_url
        print(full_path_image)

        # Save image to DB
        HeaderDao.insert_header_image(header_name_save, full_path_image)
    except Exception as error: 
        raise error
    
    return full_path_image

def clean_header_cache(url):
    """
    Clean cache save header
    """
    cache.delete(url)