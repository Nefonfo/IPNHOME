from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _

from wagtail.users.models import UserProfile

from user.models import User
from registration.forms import UserProfileForm

# Create your views here.
class UserProfileView(TemplateView):

    template_name = 'registration/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not (self.request.user.is_staff or self.request.user.is_superuser):
            UserProfile.get_for_user(self.request.user)
            student = self.request.user.student
            if student is not None:
                context['student'] = student
        return context

    def render_to_response(self, context, **response_kwargs):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return redirect(reverse('wagtailadmin_home'))
        elif self.request.user.first_name == '' or self.request.user.last_name == '':
            messages.warning(self.request, _('You need to update your First Name and/or Last Name'))
            return redirect(reverse('profile_edit'))
        else:
            return super().render_to_response(context, **response_kwargs)

class UserEditProfileView(FormView):
    template_name = 'registration/user_profile_edit.html'
    form_class = UserProfileForm

    def form_valid(self, form):
        try:
            form.save_user(User.objects.get(email = self.request.user))
            messages.success(self.request, _('Updated Successful'))
        except Exception as e:
            messages.error(self.request, _('Error: ') + str(e))
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse('profile_edit')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'email': self.request.user.email,
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name
        }
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_avatar'] = UserProfile.get_for_user(User.objects.get(email = self.request.user)).avatar
        return context
    