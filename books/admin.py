from django.contrib import admin
from books.models import Book, Author, Oppkg, Publisher, Nf, Operator, SwPackage, Subscriber

class OppkgAdmin(admin.ModelAdmin):
    search_fields = ('operator', 'sw_pkg')
    filter_horizontal = ('nfs',)

admin.site.register(Nf)
admin.site.register(Operator)
admin.site.register(SwPackage)
admin.site.register(Oppkg, OppkgAdmin)
admin.site.register(Subscriber)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Publisher)
