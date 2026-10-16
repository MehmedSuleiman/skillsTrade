from django.contrib import messages
from django.db import models
from django.db.models import Q, F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.detail import _M

from common.forms import SearchForm
from common.models import SkillCategory
from skills.forms import CreateSkillForm, EditSkillForm
from skills.models import Skill


# Create your views here.
def skills_type_view(request : HttpRequest, skills_type) -> HttpResponse:
    skills = Skill.objects.filter(category=skills_type).prefetch_related('related_skills')
    category_name = dict(SkillCategory.choices).get(skills_type, skills_type.title())
    search_form = SearchForm(request.GET or None)

    if request.method == 'GET' and search_form.is_valid():
        skills = skills.filter(
            Q(name__icontains=search_form.cleaned_data['query'])
                |
            Q(description__icontains=search_form.cleaned_data['query'])
        )

    context = {
        'skills': skills,
        'category': skills_type,
        'category_name': category_name,
        'search_form': search_form,
    }
    return render(request, 'skills/skill_type.html', context)

class SkillCreate(CreateView):
    model = Skill
    form_class = CreateSkillForm
    template_name = 'skills/create_skill.html'
    success_url = reverse_lazy('common:home')

    def form_valid(self, form):
        messages.success(self.request, "Skill successfully created")
        return super().form_valid(form)


class SkillUpdate(UpdateView):
    model = Skill
    form_class = EditSkillForm
    template_name = 'skills/update_skill.html'
    success_url = reverse_lazy('common:home')

class SkillDelete(DeleteView):
    model = Skill
    template_name = 'skills/delete_skill.html'
    success_url = reverse_lazy('common:home')

class SkillDetail(DetailView):
    model = Skill
    template_name = 'skills/skill_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.objects.update(views = F('views') + 1)
        return obj

