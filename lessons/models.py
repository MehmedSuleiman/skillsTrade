from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.text import slugify

from common.models import TimeStampModel

class Lesson(TimeStampModel):
    profile = models.ForeignKey(
        to ='accounts.Profile',
        on_delete=models.CASCADE,
        related_name='lessons',
    )

    title = models.CharField(
        max_length=110,
        validators=[
            MinLengthValidator(2)
        ],
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(20),
        ]
    )
    url = models.URLField(
        blank=True,
        null=True,
    )
    phone_number = models.CharField(
        blank=True,
        null=True,
    )

    email = models.EmailField()

    logo = models.ImageField(
        upload_to='lessons/logos/%Y/%m/%d/',
        blank=True,
        null=True,
    )

    duration_weeks = models.PositiveIntegerField()

    skills = models.ManyToManyField(
        to = 'skills.Skill',
        related_name='skills',
    )

    slug = models.SlugField(
        unique=True,
    )

    views = models.PositiveIntegerField(
        default=0,
    )

    def __str__(self) -> str:
        return self.title

    def __repr__(self) -> str:
        return self.title

    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(f"{self.title}-{self.pk}")

        super().save(*args, **kwargs)

