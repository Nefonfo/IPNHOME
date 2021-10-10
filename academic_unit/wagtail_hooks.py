from django.utils.translation import gettext_lazy as _

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from wagtail.contrib.modeladmin.mixins import ThumbnailMixin

from academic_unit.models import AcademicUnit

class AcademicUnitAdmin(ThumbnailMixin, ModelAdmin):
    model = AcademicUnit
    menu_label = _('Academic Units')
    menu_icon = 'group'
    menu_order = 100
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('admin_thumb', 'little_name', 'level')
    list_filter = ('level',)
    search_fields = ('little_name', 'name')
    list_per_page = 10

    thumb_image_field_name = 'logo'
    thumb_image_filter_spec = 'fill-300x300'

modeladmin_register(AcademicUnitAdmin)