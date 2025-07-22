# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Author(models.Model):

    #__Author_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Author_FIELDS__END

    class Meta:
        verbose_name        = _("Author")
        verbose_name_plural = _("Author")


class Book(models.Model):

    #__Book_FIELDS__
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)

    #__Book_FIELDS__END

    class Meta:
        verbose_name        = _("Book")
        verbose_name_plural = _("Book")



#__MODELS__END
