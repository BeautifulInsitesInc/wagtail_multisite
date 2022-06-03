from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

@register_setting #simply use decorator to register to show up in settings
class SocialMediaSettings(BaseSetting):
    instagram = models.URLField(max_length=100)

    panels = [
       FieldPanel("instagram"),
    ]
