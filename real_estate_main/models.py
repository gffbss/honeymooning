from django.db import models
from django.db.models import permalink

# Create your models here.


class Homess(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    property_type = models.CharFieldd(max_length=100, unique=True)
    beds = models.DecimalField()
    baths = models.IntegerField()
    price = CommaSeparatedIntegerField(max_length = none)
    category = models.ForeignKey('homess.Category')

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_homess_post', None, { 'slug': self.slug })


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_homess_category', None, { 'slug': self.slug })


# class ContactForm(models.Model):
#     name = models.CharField(max_length=200, blank=False, null=False, verbose_name="your name")
#     phone = models.CharField(max_length=200, blank=False, null=False, verbose_name="your phone")
#     email = models.EmailField(max_length=255, blank=False, null=False)
#
#     created_at = models.DateTimeField(auto_now=True)
#
#     def __unicode__(self):
#         return self.name