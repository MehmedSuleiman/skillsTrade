from django.test import TestCase
from django.urls import reverse

from common.models import SkillCategory, SkillDifficulty
from skills.models import Skill


class SkillCreateViewTests(TestCase):
    def test_create_skill_page_status_and_template(self):
        url = reverse('skills:create-skill')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'skills/create_skill.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_create_skill_renders_form_fields(self):
        url = reverse('skills:create-skill')
        response = self.client.get(url)
        self.assertContains(response, 'name="name"')
        self.assertContains(response, 'name="category"')
        self.assertContains(response, 'name="difficulty"')
        self.assertContains(response, 'name="description"')
        self.assertContains(response, 'name="badge"')
        self.assertContains(response, 'name="related_skills"')
        self.assertContains(response, 'Publish Skill')

    def test_create_skill_valid_post(self):
        url = reverse('skills:create-skill')
        data = {
            'name': 'Modern React and TypeScript',
            'category': SkillCategory.TECHNICAL,
            'difficulty': SkillDifficulty.INTERMEDIATE,
            'description': 'Comprehensive hands-on guide to mastering React, Next.js, and TypeScript.',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('common:home'))
        self.assertTrue(Skill.objects.filter(name='Modern React and TypeScript').exists())

    def test_create_skill_invalid_post_shows_errors(self):
        url = reverse('skills:create-skill')
        response = self.client.post(url, {'name': 'Hi'})
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Skill.objects.filter(name='Hi').exists())
        self.assertContains(response, 'Ensure this value has at least 5 characters')
