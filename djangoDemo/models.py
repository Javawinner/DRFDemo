from django.db import models


# Create your models here.

__all__= ["Book", "Publisher", "Author"]

class Book(models.Model):
    title = models.CharField(max_length=32)
    CHOICES = ((1, 'Python'), (2, 'Linux'), (3, 'go'))
    category = models.IntegerField(choices=CHOICES)
    pub_time = models.DateField()
    publisher = models.ForeignKey(to="Publisher")
    authors = models.ManyToManyField(to="Author")

class Publisher(models.Model):
    title = models.CharField(max_length=32)


class Author(models.Model):
    name = models.CharField(max_length=32)


