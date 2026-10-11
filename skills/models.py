from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from common.models import SkillCategory, SkillDifficulty, TimeStampModel


class Skill(TimeStampModel):
    category = models.CharField(
        max_length = 100,
        choices = SkillCategory.choices,
        default = SkillCategory.OTHER,
    )

    name = models.CharField(
        max_length = 100,
        validators=[
            MinLengthValidator(5),
        ]
    )

    difficulty = models.CharField(
        max_length = 13,
        choices = SkillDifficulty.choices,
    )

    description = models.CharField(
        blank = True,
        null = True,
        validators=[
            MinLengthValidator(20),
        ]
    )

    is_active = models.BooleanField(
        default = True,
    )

    badge = models.ImageField(
        upload_to = 'skill_badges/',
        blank = True,
        null = True,
    )

    related_skills = models.ManyToManyField(
        to = 'self',
        blank = True,
    )

    slug = models.SlugField(
        blank = True,
        unique = True,
    )

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        self.slug = slugify(f"{self.name}-{self.pk}")
        super().save(*args, **kwargs)