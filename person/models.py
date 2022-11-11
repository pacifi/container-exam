from django.db import models


class Person(models.Model):
    first_name = models.CharField(u"First Name", max_length=50)
    last_name = models.CharField(u"Last Name", max_length=50)
    avatar = models.FileField(u"Avatar", upload_to="persons_files")

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
