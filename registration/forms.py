from django.db.utils import IntegrityError
from django.core.files.images import ImageFile
from django.utils.translation import gettext_lazy as _
from django import forms

from wagtail.users.models import UserProfile

from user.models import User

class UserProfileForm(forms.Form):
    avatar = forms.ImageField(required = False, label = _('Avatar'))
    email = forms.EmailField(required = True, label = _('Email'))
    first_name = forms.CharField(min_length = 2, max_length = 150, required = True, label = _('First Name'))
    last_name = forms.CharField(min_length = 2, max_length = 150, required = True, label = _('Last Name'))

    def save_user(self, user):
        form_data = self.cleaned_data
        user_with_email = User.objects.filter(email = form_data['email'])
        if user_with_email.exists() and user.email != form_data['email']:
            raise IntegrityError(_('User Email may be unique'))
        else:
            user.email = form_data['email']
            user.first_name = form_data['first_name']
            user.last_name = form_data['last_name']
            user.save()
        if form_data['avatar'] is not None:
            user_profile = UserProfile.objects.get(user = user)
            image = ImageFile(form_data['avatar'], name = form_data['avatar'].name)
            user_profile.avatar = image
            user_profile.save()
