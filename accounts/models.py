from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.mail import send_mail
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from common.models import TimeStampModel


"""
     There ia a signal after creating a user.
"""
class AppUser(AbstractBaseUser, PermissionsMixin):

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    email = models.EmailField()

    is_school = models.BooleanField(
        default=False
    )

    is_staff = models.BooleanField(
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_active = models.BooleanField(
        default=True,
        help_text=(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(
        default=timezone.now
    )

    objects = UserManager()

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


    def __str__(self) -> str:
        return self.username

    def __repr__(self) -> str:
        return self.username


class Profile(TimeStampModel):
    user = models.OneToOneField(
        to=AppUser,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    first_name = models.CharField(
        max_length=70,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(2)
        ]
    )
    last_name = models.CharField(
        max_length=70,
        blank=True,
        null=True,
        validators=[
            MinLengthValidator(2)
        ]
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(16)
        ]
    )

    bio = models.TextField(
        blank=True,
        null=True,
    )

    profile_pic = models.ImageField(
        upload_to="profiles/profile_pic",
        blank=True,
        null=True,
    )

    skills_to_teach = models.ManyToManyField(
        to='skills.Skill',
        blank=True,
        related_name="skills_to_teach",
    )
    skills_to_learn = models.ManyToManyField(
        to='skills.Skill',
        blank=True,
        related_name="skills_to_learn",
    )

    slug = models.SlugField(
        unique=True,
    )


    def save(self, *args, **kwargs) -> None:
        self.slug = slugify(f"{self.user.username}-{self.pk}")
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.user.username

    def __repr__(self) -> str:
        return self.user.username
