from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from common.models import SchoolSkill
from .models import Course, School

@admin.register(School)
class SchoolAdmin(ModelAdmin):
    list_display = (
        "name",
        "city",
        "country",
        "email",
        "is_verified",
        "is_active",
        "updated_at",
    )
    list_filter = ("is_verified", "is_active", "country", "city")
    search_fields = ("name", "email", "city", "country", "slug")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("views", "created_at", "updated_at")
    list_editable = ("is_verified", "is_active")
    list_per_page = 25


@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = (
        "title",
        "school",
        "duration_weeks",
        "is_active",
        "views",
        "updated_at",
    )
    list_filter = ("is_active", "school", "created_at")
    search_fields = ("title", "description", "school__name", "slug")
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("school", "skills")
    readonly_fields = ("views", "created_at", "updated_at")
    list_editable = ("is_active",)
    list_per_page = 25
