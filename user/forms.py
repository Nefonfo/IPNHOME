from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from academic_unit.models import AcademicUnit

TYPE_USER_CHOICES = (
    ('S', _('Student')),
    ('T', _('Teacher')),
    ('A', _('Administrator'))
)

class CustomUserEditForm(UserEditForm):
    user_type = forms.ChoiceField(choices= TYPE_USER_CHOICES, required = True, label = _('User Type'))


class CustomUserCreationForm(UserCreationForm):
    user_type = forms.ChoiceField(choices= TYPE_USER_CHOICES, required = True, label = _('User Type'))