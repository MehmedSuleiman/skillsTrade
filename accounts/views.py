from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from accounts.models import Profile
from accounts.forms import CustomUserCreationForm, ProfileCreateForm, ProfileUpdateForm

UserModel = get_user_model()
class ProfileCreateView(CreateView):
    model = Profile
    template_name = 'accounts/profile_creating.html'
    form_class = ProfileCreateForm
    success_url = reverse_lazy('common:home')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile_update.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('common:home')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

class RegisterView(UserPassesTestMixin, SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    model = UserModel
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('accounts:login')
    success_message = 'Your account is ready. Sign in to continue.'

    def test_func(self):
        return not self.request.user.is_authenticated

class ProfileDetails(DetailView):
    model = Profile
    template_name = 'accounts/profile_details.html'
    context_object_name = 'profile'
