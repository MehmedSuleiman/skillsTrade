from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from common.models import SkillCategory


def home_page(request: HttpRequest) -> HttpResponse:
    context = {
        "skill_types": SkillCategory
    }

    return render(request, "common/home-page.html", context)