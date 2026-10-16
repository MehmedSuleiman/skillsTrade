from django.db.models import Q
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from common.forms import SearchForm
from schools.models import School


def schools_home_view(request : HttpRequest, skills_type) -> HttpResponse:
    schools = School.objects.all().prefetch_related('skills')
    search_form = SearchForm(request.GET or None)

    if request.method == 'GET' and search_form.is_valid():
        skills = schools.filter(
            Q(name__icontains=search_form.cleaned_data['query'])
                |
            Q(description__icontains=search_form.cleaned_data['query'])
        )

    context = {
        'schools': schools,
        'search_form': search_form,
    }
    return render(request, 'schools/schools.html', context)

