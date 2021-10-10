from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.urls.base import reverse

from registration.views import (
    UserProfileView,
    UserEditProfileView
)

urlpatterns = [
    path('profile/', login_required(UserProfileView.as_view()), name = 'profile'),
    path('profile/edit', login_required(UserEditProfileView.as_view()), name = 'profile_edit'),
]