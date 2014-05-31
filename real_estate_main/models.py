from django.db import models


# Create your models here.


class ContactForm(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name="your name")
    phone = models.CharField(max_length=200, blank=False, null=False, verbose_name="your phone")
    email = models.EmailField(max_length=255, blank=False, null=False)

    created_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name