from django.shortcuts import get_object_or_404
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from books.forms import NfForm, OppkgForm
from books.models import Book, Author, Oppkg, Publisher, Subscriber, Nf
from django.urls import reverse

class NfCreateView(CreateView):
    model = Nf
    form_class = NfForm
    #fields = ['name',]  # 항상 넣어줘야 함
    success_url = '/books/nf/'

class NfListView(ListView):
    model = Nf
    
class NfDetailView(DetailView):
    model = Nf
    
class NfUpdateView(UpdateView):
    model = Nf
    form_class = NfForm
    template_name = "books/nf_form.html"
    # fields = ['name',]  # 항상 넣어줘야 함
    success_url = '/books/nf/'

class NfDeleteView(DeleteView):
    model = Nf
    def get_success_url(self):
        return reverse('books:nf_list')
# 없으면 nf_confirm_delete.html 찾음

class OppkgCreate(CreateView):
    model = Oppkg  # tempalte_name 안쓰면 oppkg_form.html 임
    template_name = "books/oppkg_form.html" # 없으면 모델명_form.html
    form_class = OppkgForm
    
    def get_success_url(self):
        return reverse('books:oppkg_list')

class OppkgList(ListView):
    model = Oppkg

class OppkgDetail(DetailView):
    model = Oppkg

class OppkgUpdate(UpdateView):
    model = Oppkg
    form_class = OppkgForm
    template_name = "books/oppkg_update.html" # 헷갈리니 넣어서 분리하자.
    
    def get_success_url(self):
        return reverse('books:oppkg_list')


class OppkgDelete(DeleteView):
    model = Oppkg
    def get_success_url(self):
        return reverse('books:oppkg_list')

class SubsList(ListView):
    model = Subscriber

class SubsDetail(DetailView):
    model = Subscriber

class SubsCreate(CreateView):
    model = Subscriber  # tempalte_name 안쓰면 oppkg_form.html 임
    fields = "__all__"

    def get_success_url(self):
        return reverse('books:subs_list')

class SubsUpdate(UpdateView):
    model = Subscriber
    fields = "__all__"
    
    def get_success_url(self):
        return reverse('books:subs_list')

class SubsDelete(DeleteView):
    model = Subscriber
    def get_success_url(self):
        return reverse('books:subs_list')

#--- TemplateView
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book', 'Author', 'Publisher']
        return context


#--- ListView
class BookList(ListView):
    model = Book


class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


#--- DetailView
class BookDetail(DetailView):
    model = Book


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher
