from django.contrib import admin

from .models import User, Movie, Series

# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__', 'serial', 'season', )
    list_display_links = ('pk', '__str__', )


admin.site.register(User)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Series, SeriesAdmin)