from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index

from user.models import User

# Create your models here.
class StudentQuerySet(models.QuerySet):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None

@register_snippet
class Student(index.Indexed, models.Model):

    objects = StudentQuerySet.as_manager()

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('Students')

    no_student = models.CharField(
        verbose_name=_('student number'),
        max_length=100,
        validators=[RegexValidator(regex='^[0-9]+$', message=_('Enter a numeric value'))],
        primary_key=True
    )
    user = models.OneToOneField(
        'user.User',
        verbose_name=_('user'), 
        on_delete=models.CASCADE,
        null = True,
        blank = True,
        related_name='student'
    )
    academic_unit = models.ForeignKey(
        'academic_unit.AcademicUnit',
        on_delete=models.SET_NULL, 
        verbose_name=_('Academic Unit'),
        null = True,
        blank = False
    )

    panels = [
        FieldPanel('no_student'),
        SnippetChooserPanel('user'),
        SnippetChooserPanel('academic_unit')
    ]

    search_fields = [
        index.SearchField('no_student', partial_match=True),
    ]

    def __str__(self) -> str:
        return self.no_student


@receiver(pre_save, sender = Student)
def create_student_user(sender, instance, **kwargs):
    if instance.user is None:
        generated_email = f'{instance.no_student}@ipn.mx'
        user = User()
        user.email = generated_email
        user.set_password(instance.no_student)
        user.save()
        instance.user = user

@receiver(post_delete, sender = Student)
def delete_user_student(sender, instance, **kwargs):
    try:
        if instance.user is not None:
            instance.user.delete()
    except User.DoesNotExist:
        pass

