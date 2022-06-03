# Generated by Django 4.0.4 on 2022-06-03 03:19

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('savvy_blog', '0011_alter_savvyblogpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='savvyblogpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(template='heading_block.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.blocks.RichTextBlock())], null=True, use_json_field=None),
        ),
    ]
