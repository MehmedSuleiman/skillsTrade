from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, F
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView

from common.forms import SearchForm
from common.models import SkillCategory
from skills.forms import CreateSkillForm, EditSkillForm
from skills.models import Skill


# Create your views here.
def skills_type_view(request : HttpRequest, skills_type) -> HttpResponse:
    skills = Skill.objects.filter(category=skills_type).prefetch_related('related_skills').order_by('-views')
    category_name = dict(SkillCategory.choices).get(skills_type, skills_type.title())
    search_form = SearchForm(request.GET or None)

    if request.method == 'GET' and search_form.is_valid():
        skills = skills.filter(
            Q(name__icontains=search_form.cleaned_data['query'])
                |
            Q(description__icontains=search_form.cleaned_data['query'])
        ).order_by('-views')

    page = request.GET.get('page', 1)
    paginator = Paginator(skills, 15)
    page_obj = paginator.get_page(page)

    context = {
        'skills': skills,
        'category': skills_type,
        'category_name': category_name,
        'search_form': search_form,
        'page_obj': page_obj,
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

    def get_queryset(self):
        return super().get_queryset().prefetch_related('related_skills', 'course_set__school').order_by(
            '-views')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        Skill.objects.filter(pk=obj.pk).update(views=F('views') + 1)
        return obj

