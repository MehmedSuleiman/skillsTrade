from django.urls import path
from skills import views

app_name='skills'
urlpatterns = [
    path("create-skill/", views.SkillCreate.as_view(), name="create-skill"),
    path("edit-skill/<slug:slug>/", views.SkillUpdate.as_view(), name="update-skill"),
    path("<str:skills_type>/", views.skills_type_view , name="skills_type"),

]