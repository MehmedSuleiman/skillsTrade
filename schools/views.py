from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from common.forms import SearchForm
from schools.forms import SchoolCreatingForm, SchoolUpdateForm
from schools.models import School


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
