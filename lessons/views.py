from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, F
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, FormView, CreateView, DetailView, UpdateView, DeleteView
from common.forms import SearchForm
from .models import Lesson
from .forms import LessonCreateForm, LessonUpdateForm


class LessonsListView(ListView, FormView):
    model = Lesson
    template_name = 'lessons/lessons.html'
    form_class = SearchForm
    paginate_by = 15
    ordering = ['-views']


    def get_queryset(self):
        queryset = super().get_queryset()
        search_form = SearchForm(self.request.GET or None)

        if search_form.is_valid():
            queryset = queryset.filter(
                Q(title__icontains=search_form.cleaned_data['query'])
                |
                Q(description__icontains=search_form.cleaned_data['query'])
                |
                Q(skills__name__icontains=search_form.cleaned_data['query'])
            )

        return queryset

class LessonDetail(DetailView):
    model = Lesson
    template_name = 'lessons/lesson_detail.html'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('skills').order_by(
            '-views')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        Lesson.objects.filter(pk=obj.pk).update(views=F('views') + 1)
        return obj

class LessonCreate(LoginRequiredMixin, CreateView):
    model = Lesson
    form_class = LessonCreateForm
    template_name = 'lessons/lesson_create.html'
    success_url = reverse_lazy('accounts:profile-detail')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        response = super().form_valid(form)
        self.object.save()
        messages.success(self.request, "Lesson successfully created")
        return response

class LessonUpdate(LoginRequiredMixin, UpdateView):
    model = Lesson
    form_class = LessonUpdateForm
    template_name = 'lessons/update_lesson.html'
    def get_queryset(self):
        return super().get_queryset().filter(profile__user=self.request.user)

    def get_success_url(self):
        return reverse('lessons:detail', kwargs={'slug': self.object.slug})


class LessonDelete(LoginRequiredMixin, DeleteView):
    model = Lesson
    template_name = 'lessons/delete_lesson.html'
    success_url = reverse_lazy('common:home')

    def get_queryset(self):
        return super().get_queryset().filter(profile__user=self.request.user)
