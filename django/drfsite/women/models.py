from django.db import models

# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length = 255)
    content = models.TextField(blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    is_pub = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length = 100, db_index = True)
    
    def __str__(self):
        return self.name