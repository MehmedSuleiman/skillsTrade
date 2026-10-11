import html
from django.test import SimpleTestCase
from django.urls import reverse

from common.models import SkillCategory


class HomePageViewTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('common:home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('common:home'))
        self.assertTemplateUsed(response, 'common/home-page.html')
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_contains_skill_types_context(self):
        response = self.client.get(reverse('common:home'))
        self.assertIn('skill_types', response.context)
        self.assertEqual(response.context['skill_types'], SkillCategory)

    def test_home_page_renders_all_skill_types(self):
        response = self.client.get(reverse('common:home'))
        for _, label in SkillCategory.choices:
            self.assertContains(response, html.escape(label))

    def test_home_page_renders_heading_and_links(self):
        response = self.client.get(reverse('common:home'))
        self.assertContains(response, 'Choose Skill Type')
        self.assertContains(response, 'View Skills')
