from django import forms
from .models import Lesson


class LessonBasicForm(forms.ModelForm):
    class Meta:
        model = Lesson
        exclude = ('id', 'created_at', 'updated_at', 'profile', 'slug', 'views')
        labels = {
            'title': 'Lesson Title',
            'description': 'Lesson Description',
            'url': 'Lesson Website or Booking Link',
            'phone_number': 'Contact Phone',
            'email': 'Contact Email',
            'logo': 'Lesson Image',
            'duration_weeks': 'Duration (Weeks)',
            'skills': 'Skills Covered',
        }
        help_texts = {
            'title': 'Choose a clear title learners can find easily.',
            'description': 'Explain what learners will study and what to expect (at least 20 characters).',
            'url': 'Optional. Enter the full web address, including https://.',
            'phone_number': 'Optional. Include the country code for international learners.',
            'email': 'Provide an email address learners can use to contact you.',
            'logo': 'Optional. Upload an image to represent this lesson.',
            'duration_weeks': 'Enter the length of the lesson in weeks.',
            'skills': 'Select the skills taught in this lesson. Use Ctrl or Cmd to select multiple skills.',
        }
        error_messages = {
            'title': {'min_length': 'Lesson titles must be at least 2 characters long.'},
            'description': {'min_length': 'Please add more detail (at least 20 characters).'},
            'duration_weeks': {'min_value': 'Lesson duration must be at least 1 week.'},
        }
        widgets = {
        'title': forms.TextInput(attrs={
            'placeholder': 'e.g. Beginner Python for Data Analysis',
        }),
        'description': forms.Textarea(attrs={
            'placeholder': 'Describe the lesson, topics, and what learners will be able to do...',
            'rows': 5,
        }),
        'url': forms.URLInput(attrs={
            'placeholder': 'https://example.com/lessons',
            'autocomplete': 'url',
        }),
        'phone_number': forms.TelInput(attrs={
            'placeholder': '+1 555 010 1234',
            'autocomplete': 'tel',
        }),
        'email': forms.EmailInput(attrs={
            'placeholder': 'teacher@example.com',
            'autocomplete': 'email',
        }),
        'logo': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        'duration_weeks': forms.NumberInput(attrs={
            'placeholder': 'e.g. 6',
            'min': 1,
            'inputmode': 'numeric',
        }),
        'skills': forms.SelectMultiple(attrs={'size': 6}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['skills'].queryset = self.fields['skills'].queryset.order_by('name')

        def clean_title(self):
            title = self.cleaned_data['title'].strip()
            if len(title) < 2:
                raise forms.ValidationError('Lesson titles must contain at least 2 non-space characters.')
            return title

        def clean_description(self):
            description = self.cleaned_data['description'].strip()
            if len(description) < 20:
                raise forms.ValidationError('Please add more detail (at least 20 non-space characters).')
            return description

class LessonCreateForm(LessonBasicForm):
    ...

class LessonUpdateForm(LessonBasicForm):
    ...
