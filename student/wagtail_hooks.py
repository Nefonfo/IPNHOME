from django.utils.translation import gettext_lazy as _
from django.urls import path, reverse

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem

from student.models import Student
from student.views import StudentJsonFormView

class StudentAdmin(ModelAdmin):
    model = Student
    menu_label = _('Students')
    menu_icon = 'user'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_per_page = 10
    list_display = ('no_student', 'user', 'academic_unit_little_name')
    list_filter = ('academic_unit',)
    search_fields = ('no_student',)



    def academic_unit_little_name(self, obj):
        return obj.academic_unit.little_name
    academic_unit_little_name.short_description = _('Academic Unit')

@hooks.register('register_admin_urls')
def register_student_import_url():
    return [
        path('student/student/import_from_json/', StudentJsonFormView.as_view(), name='student_import_json'),
    ]

@hooks.register('register_admin_menu_item')
def register_student_import_url_item():
    return MenuItem(_('Bulk Students Data'), reverse('student_import_json'), icon_name='group')

modeladmin_register(StudentAdmin)
