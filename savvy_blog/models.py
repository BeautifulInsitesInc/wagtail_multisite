from turtle import title
from unicodedata import name
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet

class SavvyBlogPage(Page):
    banner_title = models.CharField(max_length=100,default='This is a savvy blog')
    snippit = models.TextField(blank=True)
    body = RichTextField(blank=True)
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = True,
        on_delete=models.SET_NULL,
        related_name='+')


    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("snippit"),
        FieldPanel("body", classname="full"),
        ImageChooserPanel("banner_image"),
    ]
        
class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(blank=True, max_length=100)
    company_name = models.CharField(blank=True, max_length=100)
    company_url = models.URLField(blank=True)
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+",
        )

