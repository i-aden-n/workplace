from django.contrib import admin

from .models import *

# Register your models here.
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_pub', )
    list_display_links = ('id', 'title', )
    list_editable = ('is_pub', )


admin.site.register(Women, WomenAdmin)
admin.site.register(Category)