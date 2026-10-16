from django.core.exceptions import ValidationError
from django.db import models

from schools.models import School
from skills.models import Skill


class SkillCategory(models.TextChoices):
    TECHNICAL = "tech", "Technical & Digital Skills"
    CREATIVE = "creat", "Creative & Artistic Skills"
    LANGUAGE = "lang", "Language & Communication Skills"
    BUSINESS = "business", "Business & Professional Skills"
    CRAFTS = "craft", "Crafts & Manual Skills"
    LIFE = "life", "Life & Personal Development"
    SPORTS = "sports", "Sports & Physical Skills"
    SOCIAL = "social", "Social & Community Skills"
    DIGITAL_LIFESTYLE = "digital_lifestyle", "Digital Lifestyle Skills"
    ACADEMIC = "acad", "Science & Academic Skills"
    SPECIALIZED = "spec", "Specialized & Niche Skills"
    OTHER = "other", "Other Skills"

class SkillDifficulty(models.TextChoices):
    BEGINNER = "1", "Beginner"
    INTERMEDIATE = "2", "Intermediate"
    ADVANCED = "3", "Advanced"

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class SchoolSkill(models.Model):
    school = models.ForeignKey(
        to =School,
        on_delete=models.CASCADE,
    )
    skill = models.ForeignKey(
        to= Skill,
        on_delete=models.CASCADE
    )

    def clean(self) -> None:
        if not self.school.is_verified:
            raise ValidationError('School is not yet verified, and can\'t post skills.')