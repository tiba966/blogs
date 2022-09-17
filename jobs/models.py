from django.db import models
from .validators import validate_file_extension, validate_image_extension
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from datetime import date
from django.core.validators import MinValueValidator

from  embed_video.fields  import  EmbedVideoField


class Replay(models.Model):
    image_bg_volunteer = models.FileField(
        validators=[validate_image_extension],
        upload_to="background/volunteer/",
    )


class About(models.Model):
    image_middle_about = models.FileField(
        validators=[validate_image_extension],
        upload_to="background/about/",
        blank=True,
        null=True,
    )
    



class Category(models.Model):
    ar_name = models.CharField(blank=False, null=False, max_length=100)
    en_name = models.CharField(blank=False, null=False, max_length=100)
    
    def __str__(self):
        return self.en_name


class Blog(models.Model):
    image_one = models.FileField(
        validators=[validate_image_extension],
        default="",
        upload_to="blogs/backgrounds/",
        blank=True,
    )

    date = models.DateField(default=date.today, blank=True)

    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    tutorial_Video = EmbedVideoField(blank=True, default="",)

    title = models.CharField(max_length=300, default="", blank=True)
    title_ar = models.CharField(max_length=300, default="", blank=True)
    authors = models.CharField(max_length=300, default="", blank=True)

    authors_ar = models.CharField(max_length=300, default="", blank=True)

    desc1 = models.CharField(max_length=200, default="", blank=True)
    desc1_ar = models.CharField(max_length=200, default="", blank=True)
    desc2 = models.TextField(max_length=40000, default="", blank=True)
    desc2_ar = models.TextField(max_length=40000, default="", blank=True)
    blank = models.CharField(max_length=600, default="", blank=True)
    blank_ar = models.CharField(max_length=600, default="", blank=True)
    desc3 = models.TextField(max_length=40000, default="", blank=True)
    desc3_ar = models.TextField(max_length=40000, default="", blank=True)
    desc4 = models.TextField(max_length=40000, default="", blank=True)
    desc4_ar = models.TextField(max_length=40000, default="", blank=True)
    desc5 = models.TextField(max_length=40000, default="", blank=True)
    desc5_ar = models.TextField(max_length=40000, default="", blank=True)
    desc6 = models.TextField(max_length=40000, default="", blank=True)
    desc6_ar = models.TextField(max_length=40000, default="", blank=True)
    subtitle = models.CharField(max_length=300, default="", blank=True)
    subtitle_ar = models.CharField(max_length=300, default="", blank=True)
    subtitle_desc1 = models.TextField(max_length=40000, default="", blank=True)
    subtitle_desc1_ar = models.TextField(
        max_length=4000, default="", blank=True
    )
    subtitle_desc2 = models.TextField(max_length=40000, default="", blank=True)
    subtitle_desc2_ar = models.TextField(
        max_length=40000, default="", blank=True
    )

    subtitle2 = models.CharField(max_length=300, default="", blank=True)
    subtitle2_ar = models.CharField(max_length=300, default="", blank=True)
    subtitle2_desc1 = models.TextField(max_length=40000, default="", blank=True)
    subtitle2_desc1_ar = models.TextField(
        max_length=40000, default="", blank=True
    )
    subtitle2_desc2 = models.TextField(max_length=40000, default="", blank=True)
    subtitle2_desc2_ar = models.TextField(
        max_length=40000, default="", blank=True
    )
    subtitle2_desc3 = models.TextField(max_length=40000, default="", blank=True)
    subtitle2_desc3_ar = models.TextField(
        max_length=40000, default="", blank=True
    )

    subtitle3 = models.CharField(max_length=300, default="", blank=True)
    subtitle3_ar = models.CharField(max_length=300, default="", blank=True)
    subtitle3_desc1 = models.TextField(max_length=40000, default="", blank=True)
    subtitle3_desc1_ar = models.TextField(
        max_length=40000, default="", blank=True
    )
    subtitle4 = models.CharField(max_length=300, default="", blank=True)
    subtitle4_ar = models.CharField(
        max_length=300, default="", blank=True
    )
    subtitle4_desc1 = models.TextField(max_length=40000, default="", blank=True)
    subtitle4_desc1_ar = models.TextField(
        max_length=40000, default="", blank=True
    )
    subtitle4_desc2 = models.TextField(max_length=40000, default="", blank=True)
    subtitle4_desc2_ar = models.TextField(
        max_length=40000, default="", blank=True
    )
  
    views = models.PositiveIntegerField(default=0, validators=[
            MinValueValidator(0)
    ])
    class Meta:
        ordering = ["-date"]




class Index(models.Model):
    text_about_index = models.TextField(
        max_length=1000,
        default="",
        blank=True,
    )
    text_about_index_ar = models.TextField(
        max_length=1000,
        default="",
        blank=True,
    )
    text_index = models.TextField(
        max_length=1000,
        default="",
        blank=True,
    )
    text_index_ar = models.TextField(
        max_length=1000,
        default="",
        blank=True,
    )
    
    
