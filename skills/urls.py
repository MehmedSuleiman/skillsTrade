from django.urls import path
from django.views.generic import detail

from skills import views

app_name='skills'
urlpatterns = [
    path("detail/<slug:slug>", views.SkillDetail.as_view(), name='detail'),
    path("create-skill/", views.SkillCreate.as_view(), name="create-skill"),
    path("edit-skill/<slug:slug>/", views.SkillUpdate.as_view(), name="update-skill"),
    path("delete-skill/<slug:slug>/", views.SkillDelete.as_view(), name="delete-skill"),
    path("<str:skills_type>/", views.skills_type_view , name="skills_type"),

]