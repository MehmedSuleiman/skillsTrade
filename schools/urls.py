from django.urls import path

from schools import views

app_name = 'schools'
urlpatterns = [
    path('', views.schools_home_view, name='schools_home'),
]