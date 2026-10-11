from django import forms

from skills.models import Skill


class BaseSkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        exclude = ['is_active', 'slug']

        labels = {
            'name': 'Skill Name',
            'category': 'Category',
            'difficulty': 'Difficulty Level',
            'description': 'Description',
            'badge': 'Skill Badge / Image',
            'related_skills': 'Related Skills',
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



