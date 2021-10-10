from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager
from django.utils.translation import gettext_lazy as _

from wagtail.snippets.models import register_snippet
from wagtail.search import index

class CustomUserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = User(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('user_type', 'A')
        assert extra_fields['is_staff']
        assert extra_fields['is_superuser']
        assert extra_fields['user_type']
        return self._create_user(email, password, **extra_fields)

# Create your models here.
@register_snippet
class User(index.Indexed, AbstractUser):

    class UserType(models.TextChoices):
        STUDENT = 'S', _('Student')
        TEACHER = 'T', _('Teacher')
        ADMIN = 'A', _('Administrator')

    username = None
    email = models.EmailField(_('Email'), unique=True)
    user_type = models.CharField(
        verbose_name=_('User Type'),
        max_length=7,
        choices=UserType.choices,
        default=UserType.STUDENT
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    search_fields = [
        index.SearchField('email', partial_match=True)
    ]