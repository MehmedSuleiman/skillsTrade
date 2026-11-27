from django.urls import path
from lessons import views

app_name = 'lessons'

urlpatterns = [
    path('', views.LessonsListView.as_view(), name='lessons'),
    path('create/', views.LessonCreate.as_view(), name='create'),
    path('update/<slug:slug>/', views.LessonUpdate.as_view(), name='update'),
    path('delete/<slug:slug>/', views.LessonDelete.as_view(), name='delete'),
    path('<slug:slug>/', views.LessonDetail.as_view(), name='detail'),
]
