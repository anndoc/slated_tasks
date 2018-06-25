from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Ownable(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Author"),
                             related_name="%(class)ss", on_delete=models.CASCADE)

    class Meta:
        abstract = True


class RegisteredUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='registered_user')
    tracking = models.ManyToManyField('self',
                                      related_name='tracked_by',
                                      blank=True, symmetrical=False)


class FeedItem(Ownable):
    content = models.CharField("Content", max_length=1000,
                               blank=True, null=True)
