from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import Profile

UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'username', 'is_school')


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'age',
            'bio',
            'profile_pic',
            'skills_to_teach',
            'skills_to_learn',
        )

        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'e.g. Simon',
                'autocomplete': 'given-name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'e.g. Smith',
                'autocomplete': 'family-name',
            }),
            'age': forms.NumberInput(attrs={
                'min': 16,
                'placeholder': 'At least 16',
                'inputmode': 'numeric',
            }),
            'bio': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Share a little about yourself, your experience, and what you enjoy teaching or learning.',
            }),
            'profile_pic': forms.ClearableFileInput(attrs={
                'accept': 'image/*',
            }),
            'skills_to_teach': forms.SelectMultiple(attrs={
                'size': 7,
            }),
            'skills_to_learn': forms.SelectMultiple(attrs={
                'size': 7,
            }),
        }

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'age': 'Age',
            'bio': 'About you',
            'profile_pic': 'Profile photo',
            'skills_to_teach': 'Skills I can teach',
            'skills_to_learn': 'Skills I want to learn',
        }

        help_texts = {
            'age': 'You must be at least 16 years old.',
            'bio': 'A short introduction helps other members get to know you.',
            'profile_pic': 'Choose an image to represent your profile.',
            'skills_to_teach': 'Select one or more skills you are happy to teach.',
            'skills_to_learn': 'Select the skills you would like to learn.',
        }

class ProfileCreateForm(ProfileBaseForm):
    ...

class ProfileUpdateForm(ProfileBaseForm):
    ...
