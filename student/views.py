from django.views.generic import FormView
from django.utils.translation import gettext_lazy as _
from django.shortcuts import redirect
from django.urls import reverse
from django.db import transaction, IntegrityError

from wagtail.admin import messages

import json

from academic_unit.models import AcademicUnit
from student.forms import StudentJsonForm
from student.models import Student
from user.models import User

class StudentJsonFormView(FormView):
    template_name = 'wagtailadmin/students/import_json.html'
    form_class = StudentJsonForm

    def form_valid(self, form):
        file = self.request.FILES['file_json']
        try:
            data = json.load(file)
            with transaction.atomic():
                for element in data['data']:
                    if Student.objects.filter(no_student = element['no_student']).exists():
                        raise IntegrityError(_('Student: Primary Key duplicate'))
                    student = Student(
                        no_student = element['no_student'],
                        academic_unit = AcademicUnit.objects.get(little_name = element['academic_unit'])
                    )

                    student.save()
                    print(student)
                    user = User.objects.get(pk = student.user.id)
                    if 'email' in element.keys():
                        user.email = element['email']
                    if 'first_name' in element.keys():
                        user.first_name = element['first_name']
                    if 'last_name' in element.keys():
                        user.last_name = element['last_name']
                    user.save()
            messages.success(self.request, _('Database Uploaded Successfully'))
            pass
        except Exception as e:
            print(e)
            messages.error(self.request, '{}: {}'.format(_("Error: "), str(e)))
        return redirect(reverse('student_import_json'))

    def form_invalid(self, form):
        messages.error(self.request, _('Form Error: Please, check file extension'))
        return super().form_invalid(form)