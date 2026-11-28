from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy
from accounts import views
app_name='accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile-create', views.ProfileCreateView.as_view(), name='profile-create'),
    path('profile/<slug:slug>/', views.ProfileDetails.as_view(), name='profile-detail'),
    path('profile-update/<int:pk>', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('password-change/', PasswordChangeView.as_view(
        success_url=reverse_lazy('accounts:password_change_done'),
    ), name='password_change'),
    path('password-change-done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password-reset/', PasswordResetView.as_view(
        email_template_name='registration/password_reset_email.txt',
        html_email_template_name='registration/password_reset_email.html',
    ), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirmed'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
