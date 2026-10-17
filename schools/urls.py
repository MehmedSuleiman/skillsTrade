from django.urls import path, include

from schools import views

app_name = 'schools'
urlpatterns = [
    path('', views.schools_home_view, name='schools_home'),
    path('detail/<slug:slug>', views.SchoolDetailView.as_view(), name='detail'),
    path('create/', views.SchoolCreate.as_view(), name='create_school'),
    path('update/<slug:slug>', views.SchoolUpdate.as_view(), name='update_school'),
    path('delete/<slug:slug>', views.SchoolDelete.as_view(), name='delete_school'),
    path('courses/', include([
        path('', views.CourseListView.as_view(), name='course_list'),
    ]))
]