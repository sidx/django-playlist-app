from django.contrib import admin

from .models import songModel, genreModel

# Register your models here.
admin.site.register(songModel)
admin.site.register(genreModel)
