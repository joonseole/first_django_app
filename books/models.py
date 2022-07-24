from django.db import models
from django.urls import reverse
import gettext as _

class Nf(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Operator(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class SwPackage(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name

class Oppkg(models.Model):
    operator = models.ForeignKey(Operator, on_delete=models.SET_NULL, null=True)
    sw_pkg = models.ForeignKey(SwPackage, on_delete=models.SET_NULL, null=True)
    nfs = models.ManyToManyField(Nf)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    class Meta:
        verbose_name = 'Operator & Package'
        ordering = ['created_at',]

    def __str__(self) -> str:
        return self.operator.name + " : " + self.sw_pkg.name
    
class Subscriber(models.Model):
    oppkg = models.ForeignKey(Oppkg, on_delete=models.CASCADE)
    year = models.IntegerField()
    num_5gm = models.IntegerField()
    num_4gm = models.IntegerField()
    num_5gf = models.IntegerField()

    class Meta:
        verbose_name = '가입자수와 Tput'
        ordering = ['oppkg', 'year']

    def __str__(self) -> str:
        return self.oppkg.operator.name + " : " + self.oppkg.sw_pkg.name + " (Year " + str(self.year) + ")"


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
