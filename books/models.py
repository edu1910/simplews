from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name

class Book(models.Model):
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    title = models.CharField(max_length=100)
    description = models.TextField()
    def __unicode__(self):
        return self.title

