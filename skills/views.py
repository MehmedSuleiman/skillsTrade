from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.models import SkillCategory
from skills.forms import CreateSkillForm
from skills.models import Skill


# Create your views here.
def skills_type_view(request : HttpRequest, skills_type) -> HttpResponse:
    skills = Skill.objects.filter(category=skills_type).prefetch_related('related_skills')
    category_name = dict(SkillCategory.choices).get(skills_type, skills_type.title())

    context = {
        'skills': skills,
        'category': skills_type,
        'category_name': category_name,
    }
    return render(request, 'skills/skill_types.html', context)

class SkillCreate(CreateView):
    model = Skill
    form_class = CreateSkillForm
    template_name = 'skills/create_skill.html'
    success_url = reverse_lazy('common:home')