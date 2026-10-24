from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Skill


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = (
        "name",
        "category",
        "difficulty",
        "is_active",
        "views",
        "updated_at",
    )
    list_filter = ("category", "difficulty", "is_active", "created_at")
    search_fields = ("name", "description", "slug")
    prepopulated_fields = {"slug": ("name",)}
    filter_horizontal = ("related_skills",)
    readonly_fields = ("views", "created_at", "updated_at")
    list_editable = ("is_active",)
    list_per_page = 25
