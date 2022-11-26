from django.urls import path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('register', Register.as_view(), name = 'register'),
    path('login', Login.as_view(), name = 'login'),
    path('logout', logout_user, name = 'logout'),
    path('profile/<slug:username>', Profile.as_view(), name = 'proflie'),
    path('create-klass', CreateKlass.as_view(), name = 'create_klass'),
    path('klassy', Klassy.as_view(), name = 'klassy'),
    path('exact-klass/<slug:klass_slug>', ExatKlass.as_view(), name = 'exact_klass'),
    path('create-exam-tables', CreateExamTable.as_view(), name = 'create_exam_tables'),
    path('edit-exam-tables/<slug:exam_table_slug>', edit_exam_table, name = 'edit_exam_tables'),
    path('remote', Remote.as_view(), name = 'remote')
]