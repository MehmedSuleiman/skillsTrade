from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.utils.text import slugify

from common.models import TimeStampModel, SchoolSkill
from skills.models import Skill


class School(TimeStampModel):
    name = models.CharField(
        max_length=100,
        unique=True,
        validators=[
            MinLengthValidator(4),
        ]
    )

    description = models.TextField(
        validators=[MinLengthValidator(20)],
    )

    logo = models.ImageField(
        upload_to='schools/logos/',
        blank=True,
        null=True,
    )

    website = models.URLField(
        blank=True,
        null=True,
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=30
    )

    city = models.CharField(
        max_length=100
    )
    country = models.CharField(
        max_length=100
    )

    address = models.CharField(
        max_length=255,
    )

    is_verified = models.BooleanField(default=True)  #TODO : when learn how to manage roles, default must be false
    is_active = models.BooleanField(default=True)

    founded_year = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    skills = models.ManyToManyField(
        to = Skill,
        through =SchoolSkill
    )

    slug = models.SlugField(
        unique=True
    )

    views = models.PositiveIntegerField(
        default = 0,
    )


    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name


    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        self.slug = slugify(f"{self.name}-{self.pk}")
        super().save(*args, **kwargs)

class Course(TimeStampModel):
    school = models.ForeignKey(
        to =School,
        on_delete=models.CASCADE,
        related_name='courses',
    )

    title = models.CharField(
        max_length=110
    )
    description = models.TextField(
        validators=[
            MinLengthValidator(20),
        ]
    )
    url = models.URLField()

    logo = models.ImageField(
        upload_to='courses/logos/',
    )

    duration_weeks = models.PositiveIntegerField()

    skills = models.ManyToManyField(
        to = Skill
    )

    is_active = models.BooleanField(
        default=True
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
        super().save(*args, **kwargs)
        self.slug = slugify(f"{self.title}-{self.pk}")
        super().save(*args, **kwargs)

