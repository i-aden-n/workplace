from django.contrib import admin

from .models import User, Klass, ExamTable


# Register your models here.
class KlassAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(User)
admin.site.register(Klass, KlassAdmin)
admin.site.register(ExamTable)
