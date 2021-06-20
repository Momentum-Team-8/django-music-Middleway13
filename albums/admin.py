from django.contrib import admin
from .models import Album
from albums.models import Album
# Register your models here.
admin.site.register(Album)