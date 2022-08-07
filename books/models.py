from django.db import models
from django.urls import reverse
import gettext as _
from django.contrib.auth.models import User

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
    sess_5gm = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Operators and Packages'
        ordering = ['created_at',]

    def __str__(self) -> str:
        return self.operator.name + " : " + self.sw_pkg.name
    
    def get_absolute_url(self):
        return reverse("books:oppkg_detail", kwargs={"pk": self.pk})
    
    
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
    
    def get_absolute_url(self):
        return reverse("books:subs_detail", kwargs={"pk": self.pk})
    


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    publication_date = models.DateField()

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('books:book_detail', args=[self.pk])
        # return reverse('books:book_detail', kwargs={'pk':self.pk}) 와 동일

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
