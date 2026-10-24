from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import SchoolSkill


@admin.register(SchoolSkill)
class SchoolSkillAdmin(ModelAdmin):
    list_display = ("school", "skill")
    list_filter = ("school__country", "skill__category")
    search_fields = ("school__name", "skill__name")
    autocomplete_fields = ("school", "skill")
    list_select_related = ("school", "skill")
    list_per_page = 25
