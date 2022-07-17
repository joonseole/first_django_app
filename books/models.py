from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.pk])
        # return reverse('books:book_detail', kwargs={'pk':self.pk})

class Author(models.Model):
    name = models.CharField(max_length=50)
    salutation = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('books:author_detail', args=[self.pk])


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    website = models.URLField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('books:publisher_detail', args=[self.pk])
