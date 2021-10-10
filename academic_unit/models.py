from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index

# Create your models here.
@register_snippet
class AcademicUnit(index.Indexed, models.Model):

    class Meta:
        verbose_name = _('Academic Unit')
        verbose_name_plural = _('Academic Units')

    class Level(models.TextChoices):
        MEDIA_SUPERIOR = 'MS', _('HighSchool')
        SUPERIOR = 'S', _('University')
        DAE = 'DAE', _('DAE')

    name = models.CharField(
        max_length=255,
        verbose_name=_('Academic Unit Name'),
        unique=True
    )
    little_name = models.CharField(
        max_length = 100,
        verbose_name=_('Abbreviation Name'),
        unique=True
    )
    level = models.CharField(
        verbose_name=_('Level'),
        max_length=3,
        choices=Level.choices,
        default=Level.SUPERIOR,
    )
    logo = models.ForeignKey(
        'wagtailimages.Image',
        verbose_name=_('Academic Unit Logo'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('level'),
        ImageChooserPanel('logo')
    ]

    search_fields = [
        index.SearchField('name', partial_match=True),
        index.SearchField('little_name', partial_match=True)
    ]

    def __str__(self):
        return self.name