from django.db.models import TextField
from django_base_publications.models import BasePublication
from django.utils.translation import gettext_lazy as _


class News(BasePublication):
    content = TextField(
        verbose_name=_('Content'),
    )

    def get_absolute_url(self):
        return ''

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
