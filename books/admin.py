from django.contrib import admin
from books.models import Book, Author, Oppkg, Publisher, Nf, Operator, SwPackage, Subscriber

admin.site.register(Nf)
admin.site.register(Operator)
admin.site.register(SwPackage)
admin.site.register(Oppkg)
admin.site.register(Subscriber)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
