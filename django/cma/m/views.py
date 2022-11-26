import datetime

from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from django.views.generic import TemplateView, CreateView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import DetailView, ListView

from .utils import DataMixin, SuperUserRequiredMixin
from .forms import RegisterForm, LoginForm, KlassForm, ExamTableForm, MarksFormset
from .models import Klass, User, ExamTable, Marks

# Create your views here.
class Home(DataMixin, LoginRequiredMixin, TemplateView):
    template_name = 'm/home.html'
    login_url = 'login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Home'
        )
        context.update(c_cont)
        return context


class Register(SuperUserRequiredMixin, DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'm/formas.html'
    success_url = reverse_lazy('register')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Register Student',
        )
        context.update(c_cont)
        return context


class Login(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'm/formas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Login'
        )
        context.update(c_cont)
        return context


class Profile(DataMixin, DetailView):
    model = User
    template_name = 'm/profile.html'
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = context['user'].username
        )
        context.update(c_cont)
        return context

    def get_object(self):
        return User.objects.get(username = self.kwargs['username'])


class CreateKlass(DataMixin, SuperUserRequiredMixin, CreateView):
    form_class = KlassForm
    template_name = 'm/formas.html'
    success_url = reverse_lazy('create_class')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title ='Create Klass',   
        )
        context.update(c_cont)
        return context
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.slug = form.name.lower().replace(' ', '-')
        print(form.slug)
        return redirect('create_klass')


class Klassy(DataMixin, ListView):
    model = Klass
    template_name = 'm/klassy.html'
    context_object_name = 'klassy'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'klassy'
        )
        context.update(c_cont)
        return context


class Remote(DataMixin, TemplateView):
    template_name = 'm/remote.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'remote',
            options = [
                {'url': 'register', 'name': 'register'},
                {'url': 'create_klass', 'name': 'create klass'},
                {'url': 'home', 'name': 'home'},
                {'url': 'create_exam_tables', 'name': 'create exam table'},
            ]
        )
        context.update(c_cont)
        return context


class CreateExamTable(DataMixin, CreateView):
    form_class = ExamTableForm
    template_name = 'm/formas.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Exam Table Creation'
        )
        context.update(c_cont)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.slug = f'{instance.for_klass}-{datetime.datetime.now().strftime("%Y%m%d%H%M%S")}'
        instance.save()
        for i in instance.for_klass.users.all():
            mark = Marks(student = i, exam_table = instance)
            mark.save()
        return redirect('create_exam_tables')


class EditExamTable(DataMixin, FormView):
    template_name = 'm/edit_exam_table.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'Edit Exam Table'
        )
        context.update(c_cont)
        return context
    
    def get_form(self):
        return MarksFormset(queryset=ExamTable.objects.get(slug = self.kwargs['exam_table_slug']).table_lines.all())


class ExatKlass(DataMixin, DetailView):
    model = Klass
    template_name = 'm/exact-klass.html'
    context_object_name = 'klass'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_cont = self.get_user_context(
            title = 'some klass',
            last_exam = context['klass'].exam_tables.last()
        )
        context.update(c_cont)
        return context
    
    # def get_form(self):
    #     return MarksFormset(queryset = self.get_object().exam_tables.last().table_lines.all())
    
    def get_object(self):
        return Klass.objects.get(slug = self.kwargs['klass_slug'])


def logout_user(request):
    logout(request)
    return redirect('login')

def edit_exam_table(request, exam_table_slug):
    qs = ExamTable.objects.get(slug = exam_table_slug).table_lines.all()
    if request.method == 'POST':
        form = MarksFormset(request.POST, request.FILES, queryset=qs)
        print(form)
    
    formset = MarksFormset(queryset=qs)
    context = {
        'message': 'heey'
    }
    data = DataMixin()
    data.__setattr__('request', request)
    c_cont = data.get_user_context(
        title = 'heey',
        form = formset
    )
    context.update(c_cont)
    return render(request, 'm/edit_exam_table.html', context=context)