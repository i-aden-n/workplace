from django.db import models
from django.urls import reverse

from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phonenumber = models.CharField(max_length = 255, default = '+996-999-999-999')
    balance = models.IntegerField(null = True)
    bio = models.TextField(blank = True)
    klass = models.ForeignKey('Klass', on_delete = models.CASCADE, related_name = 'users', null = True)

    def get_absolute_url(self):
        return reverse('proflie', kwargs = {'username': self.username})

class Klass(models.Model):
    name = models.CharField(max_length = 255)
    slug = models.SlugField(db_index = True)
    level = models.IntegerField(default = 1)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('exact_klass', kwargs = {'klass_slug': self.slug})


class ExamTable(models.Model):
    slug = models.SlugField()
    create_time = models.DateTimeField(auto_now_add = True)
    for_klass = models.ForeignKey('Klass', related_name = 'exam_tables', on_delete = models.CASCADE)
    
    def __str__(self):
        return (f'{self.slug} exam table')
    
    def get_editing_url(self):
        return reverse('edit_exam_tables', kwargs = {'exam_table_slug': self.slug})


class Marks(models.Model):
    student = models.ForeignKey('User', related_name = 'marks', on_delete = models.CASCADE)
    grammar = models.IntegerField(null = True)
    writing = models.IntegerField(null = True)
    listening = models.IntegerField(null = True)
    speaking = models.IntegerField(null = True)
    exam_table = models.ForeignKey('ExamTable', related_name = 'table_lines', on_delete = models.CASCADE)
    
    def __str__(self): 
        return f'{self.student} marks'