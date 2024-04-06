from django.db import models


# Create your models here.
class Links(models.Model):
    address = models.CharField(max_length=200, null=True, blank=True)
    stringname = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.stringname)
