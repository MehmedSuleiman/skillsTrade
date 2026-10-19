from django import forms

from schools.models import School, Course


class BaseSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        exclude = [
            'is_verified',
            'is_active',
            'slug',
            'views',
            'created_at',
            'updated_at',
        ]

        labels = {
            'name': 'School Name',
            'description': 'School Description',
            'logo': 'School Logo',
            'website': 'School Website',
            'email': 'School Email',
            'phone': 'School Phone',
            'city': 'School City',
            'country': 'School Country',
            'address': 'School Address',
            'founded_year': 'School Founded Year',
            'skills': 'School Skills',
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Central Academy of Technology',
                'autocomplete': 'organization',
                }
            ),
            'description': forms.Textarea(attrs={
                'placeholder': 'Tell learners about your school, its programs, and the skills it offers...',
                'rows': 5,
                }
            ),
            'logo': forms.ClearableFileInput(attrs={
                'accept': 'image/*',
                }
            ),
            'website': forms.URLInput(attrs={
                'placeholder': 'https://example.edu',
                'autocomplete': 'url',
                }
            ),
            'email': forms.EmailInput(attrs={
                'placeholder': 'contact@example.edu',
                'autocomplete': 'email',
                }
            ),
            'phone': forms.TelInput(attrs={
                'placeholder': '+1 555 010 1234',
                'autocomplete': 'tel',
                }
            ),
            'city': forms.TextInput(attrs={
                'placeholder': 'e.g. Sofia',
                'autocomplete': 'address-level2',
                }
            ),
            'country': forms.TextInput(attrs={
                'placeholder': 'e.g. Bulgaria',
                'autocomplete': 'country-name',
                }
            ),
            'address': forms.TextInput(attrs={
                'placeholder': 'Street address and building',
                'autocomplete': 'street-address',
                }
            ),
            'founded_year': forms.NumberInput(attrs={
                'placeholder': 'e.g. 1998',
                'min': 1,
                'max': 2026,
                'inputmode': 'numeric',
                }
            ),
            'skills': forms.SelectMultiple(attrs={
                'size': 6,
                }
            ),
        }

class SchoolCreatingForm(BaseSchoolForm):
    class Meta(BaseSchoolForm.Meta):

        help_texts = {
            'name': 'Use the school’s official or commonly recognized name.',
            'description': 'Describe the school and its learning community (at least 20 characters).',
            'logo': 'Optional. Upload a clear image to represent your school.',
            'website': 'Optional. Enter the full web address, including https://.',
            'email': 'Use an email address where learners can contact the school.',
            'phone': 'Include the country code so learners can reach you internationally.',
            'city': 'Enter the city where the school is located.',
            'country': 'Enter the country where the school is located.',
            'address': 'Provide the street address or campus location.',
            'founded_year': 'Optional. Enter the year the school was founded.',
            'skills': 'Select the skills offered at this school. Use Ctrl or Cmd to select multiple skills.',
        }


class SchoolUpdateForm(BaseSchoolForm):
    class Meta(SchoolCreatingForm.Meta):
        widgets = {
            **BaseSchoolForm.Meta.widgets,
            'name': forms.TextInput(attrs={
                'placeholder': 'e.g. Central Academy of Technology',
                'autocomplete': 'organization',
                'readonly': 'readonly',
            }),
        }

        help_texts = {
            **SchoolCreatingForm.Meta.help_texts,
            'name': 'School names cannot be changed after creation.',
        }


class BaseCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = [
            'is_active',
            'slug',
            'views',
            'created_at',
            'updated_at',
        ]
        labels = {
            'school': 'School',
            'title': 'Course Title',
            'description': 'Course Description',
            'url': 'Course Website',
            'logo': 'Course Image',
            'duration_weeks': 'Duration (Weeks)',
            'skills': 'Skills Covered',
        }
        help_texts = {
            'school': 'Choose the school that offers this course.',
            'title': 'Use a clear title that learners can find easily.',
            'description': 'Explain what learners will study and be able to do (at least 20 characters).',
            'url': 'Enter the full course web address, including https://.',
            'logo': 'Optional. Upload an image to represent this course.',
            'duration_weeks': 'Enter the course length in weeks.',
            'skills': 'Select the skills covered by this course. Use Ctrl or Cmd to select multiple skills.',
        }
        widgets = {
            'school': forms.Select(),
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. Introduction to Web Development',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe the course, topics, and learning outcomes...',
                'rows': 5,
            }),
            'url': forms.URLInput(attrs={
                'placeholder': 'https://example.edu/course',
                'autocomplete': 'url',
            }),
            'logo': forms.ClearableFileInput(attrs={
                'accept': 'image/*',
            }),
            'duration_weeks': forms.NumberInput(attrs={
                'placeholder': 'e.g. 8',
                'min': 1,
                'inputmode': 'numeric',
            }),
            'skills': forms.SelectMultiple(attrs={
                'size': 6,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['logo'].required = False
        self.fields['school'].queryset = School.objects.order_by('name')
        self.fields['skills'].queryset = self.fields['skills'].queryset.order_by('name')


class CourseCreatingForm(BaseCourseForm):
    ...


class CourseUpdateForm(BaseCourseForm):
    class Meta(BaseCourseForm.Meta):
        widgets = {
            **BaseCourseForm.Meta.widgets,
            'title': forms.TextInput(attrs={
                'placeholder': 'e.g. Introduction to Web Development',
                'readonly': 'readonly',
            }),
        }
        help_texts = {
            **BaseCourseForm.Meta.help_texts,
            'title': 'Course titles cannot be changed after creation.',
        }


