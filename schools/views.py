from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView, FormView

from common.forms import SearchForm
from schools.forms import SchoolCreatingForm, SchoolUpdateForm, CourseCreatingForm, CourseUpdateForm
from schools.models import School, Course


def schools_home_view(request : HttpRequest) -> HttpResponse:
    schools = School.objects.all().prefetch_related('skills').order_by('-views')
    search_form = SearchForm(request.GET or None)

    if request.method == 'GET' and search_form.is_valid():
        schools = schools.filter(
            Q(name__icontains=search_form.cleaned_data['query'])
                |
            Q(description__icontains=search_form.cleaned_data['query'])
        )

    page = request.GET.get('page', 1)
    paginator = Paginator(schools, 15)
    page_obj = paginator.get_page(page)


    context = {
        'schools': schools,
        'search_form': search_form,
        'page_obj': page_obj,
    }
    return render(request, 'schools/schools.html', context)

class SchoolDetailView(DetailView):
    model = School
    template_name = 'schools/school_detail.html'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('skills', 'courses').order_by(
            '-views')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        School.objects.filter(pk=obj.pk).update(views=F('views') + 1)
        return obj

class SchoolCreate(CreateView):
    model = School
    form_class = SchoolCreatingForm
    template_name = 'schools/school_create.html'
    success_url = reverse_lazy('schools:schools_home')

class SchoolUpdate(UpdateView):
    model = School
    form_class = SchoolUpdateForm
    template_name = 'schools/school_edit.html'
    success_url = reverse_lazy('schools:schools_home')

class SchoolDelete(DeleteView):
    model = School
    template_name = 'schools/confirm_delete.html'
    success_url = reverse_lazy('schools:schools_home')

class CourseListView(ListView, FormView):
    model = Course
    template_name = 'schools/courses/course_list.html'
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
                Q(school__name__icontains=search_form.cleaned_data['query'])
            )

        return queryset


class CourseDetailView(DetailView):
    model = Course
    template_name = 'schools/courses/course_detail.html'

    def get_queryset(self):
        return super().get_queryset().select_related('school').prefetch_related('skills')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        Course.objects.filter(pk=obj.pk).update(views=F('views') + 1)
        return obj

class CourseCreate(CreateView):
    model = Course
    form_class = CourseCreatingForm
    template_name = 'schools/courses/course_create.html'

    def get_school(self):
        return get_object_or_404(School, slug=self.kwargs['school_slug'])

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        school = self.get_school()
        if school:
            form.fields['school'].initial = school.pk
            form.fields['school'].disabled = True
        return form

    def form_valid(self, form):
        school = self.get_school()
        if school:
            form.instance.school = school
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['school'] = self.get_school()
        return context

    def get_success_url(self):
        return reverse('schools:course_detail', kwargs={'slug': self.object.slug})


class CourseUpdate(UpdateView):
    model = Course
    form_class = CourseUpdateForm
    template_name = 'schools/courses/course_edit.html'

    def get_success_url(self):
        return reverse('schools:course_detail', kwargs={'slug': self.object.slug})


class CourseDelete(DeleteView):
    model = Course
    template_name = 'schools/courses/course_confirm_delete.html'

    def get_queryset(self):
        return super().get_queryset().select_related('school')

    def get_success_url(self):
        return reverse('schools:detail', kwargs={'slug': self.object.school.slug})

