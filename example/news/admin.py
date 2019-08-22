from django.contrib import admin
from django_base_publications.admin import PublicationAdmin

from .models import News


class NewsAdmin(PublicationAdmin):
    fieldsets = (
        *PublicationAdmin.fieldsets,
        ('Content', {'fields': ('content',)}),
    )


admin.site.register(News, NewsAdmin)
