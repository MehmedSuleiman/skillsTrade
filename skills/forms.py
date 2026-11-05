from django import forms

from skills.models import Skill


class BaseSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['is_active', 'slug', 'views']

        labels = {
            'name': 'Skill Name',
            'category': 'Category',
            'difficulty': 'Difficulty Level',
            'description': 'Description',
            'badge': 'Skill Badge / Image',
            'related_skills': 'Related Skills',
        }

        error_messages = {
            'name': {
                'min_length': 'Skill names must be at least 5 characters long.',
                'unique': 'A skill with this name already exists. Try a more specific name.',
            },
            'description': {
                'min_length': 'Please add a little more detail (at least 20 characters).',
            },
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Django Web Development, Jazz Guitar Basics',
                }
            ),
            'category': forms.Select(),
            'difficulty': forms.Select(),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Describe what you will teach, session expectations, and what you would like to learn in return...',
                    'rows': 4,
                }
            ),
            'badge': forms.ClearableFileInput(
                attrs={
                    'accept': 'image/*',
                }),
            'related_skills': forms.SelectMultiple(),
        }

    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        if len(name) < 5:
            raise forms.ValidationError('Skill names must contain at least 5 non-space characters.')
        return name

    def clean_description(self):
        description = (self.cleaned_data.get('description') or '').strip()
        if description and len(description) < 20:
            raise forms.ValidationError('Please add a little more detail (at least 20 characters).')
        return description



class CreateSkillForm(BaseSkillForm):
    class Meta(BaseSkillForm.Meta):

        help_texts = {
            'name': 'Minimum 5 characters. Be clear and descriptive.',
            'category': 'Determines where learners discover your skill.',
            'difficulty': 'Helps peers gauge prerequisite experience.',
            'description': 'Describe what you will teach and exchange expectations (min. 20 chars).',
            'badge': 'Optional. Upload an image or badge for your skill.',
            'related_skills': 'Optional. Hold Ctrl (Windows) or Cmd (Mac) to select multiple related skills.',
        }


class EditSkillForm(BaseSkillForm):

    class Meta(BaseSkillForm.Meta):
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'e.g. Django Web Development, Jazz Guitar Basics',
                    'readonly': 'readonly',
                }
            ),
            'category': forms.Select(),
            'difficulty': forms.Select(),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Describe what you will teach, session expectations, and what you would like to learn in return...',
                    'rows': 4,
                }
            ),
            'badge': forms.ClearableFileInput(
                attrs={
                    'accept': 'image/*',
                }),
            'related_skills': forms.SelectMultiple(),
        }

        help_texts = {
            'name': 'You can\'t edit your skill name.',
            'category': 'Determines where learners discover your skill.',
            'difficulty': 'Helps peers gauge prerequisite experience.',
            'description': 'Describe what you will teach and exchange expectations (min. 20 chars).',
            'badge': 'Optional. Upload an image or badge for your skill.',
            'related_skills': 'Optional. Hold Ctrl (Windows) or Cmd (Mac) to select multiple related skills.',

        }





