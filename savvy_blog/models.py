from email.mime import image
from turtle import title
from unicodedata import name
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel

class SavvyBlogPage(Page):
    banner_title = models.CharField(max_length=100,default='This is a savvy blog')
    
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null = True,
        blank = True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    snippet = models.TextField(blank=True)
    author =  models.ForeignKey(
        "Author", #refering to the Class
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField([
        #('name', blocks.SomthingsBlock()),
        ('heading', blocks.CharBlock(template='heading_block.html')), #can style this with css or give it a template: blocks.CharBlock(template="headings-block.html")
        ('image', ImageChooserBlock()),
        ('paragraph', blocks.RichTextBlock()),
    ], null=True)


    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        ImageChooserPanel("banner_image"),
        FieldPanel("snippet"),
        StreamFieldPanel("body"),
        SnippetChooserPanel("author"),

    ]

@register_snippet   #Use decorator to register class as a snippet 
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

    panels = [
        FieldPanel("name"),
        FieldPanel("title"),
        FieldPanel("company_name"),
        FieldPanel("company_url"),
        ImageChooserPanel("image"),
    ]

    def __str__(self):
        return self.name
