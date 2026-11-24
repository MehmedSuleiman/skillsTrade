from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name='accounts'

urlpatterns = [
    path('cbv/login/', LoginView.as_view(), name='login'),
    path('cbv/logout/', LogoutView.as_view(), name='logout'),
]