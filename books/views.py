from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from books.forms import NfForm, OppkgForm, SubsInlineFormSet
from books.models import Book, Author, Oppkg, Publisher, Subscriber, Nf
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.contrib import messages

class NfListView(ListView):
    model = Nf
    
class NfDetailView(DetailView):
    model = Nf

class NfCreateView(LoginRequiredMixin, CreateView):
    model = Nf
    form_class = NfForm
    #fields = ['name',]  # 항상 넣어줘야 함
    success_url = '/books/nf/'

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

class OppkgList(ListView):
    model = Oppkg

    def get_context_data(self, **kwargs):
        context = super(OppkgList, self).get_context_data()
        context['subscribers'] = Subscriber.objects.all()
        return context

# OppkgList를 상속받아 오버라이딩
class OppkgSearch(OppkgList):
    def get_queryset(self):
        q = self.kwargs['q']
        oppkg_list = Oppkg.objects.filter(
            Q(operator__name__contains=q) | Q(sw_pkg__name__contains=q) | Q(nfs__name__contains=q)
        ).distinct()
        return oppkg_list
        
    def get_context_data(self, **kwargs):
        context = super(OppkgSearch, self).get_context_data()
        q = self.kwargs['q']
        context['search_info'] = f'Search: {q} ({self.get_queryset().count()})'
        return context

class OppkgDetail(DetailView):
    model = Oppkg

    def get_context_data(self, **kwargs):
        context = super(OppkgDetail, self).get_context_data()
        context['subscribers'] = Subscriber.objects.filter(oppkg__pk=self.kwargs['pk'])
        return context

class OppkgCreate(LoginRequiredMixin, CreateView):
    model = Oppkg  # tempalte_name 안쓰면 oppkg_form.html 임
    template_name = "books/oppkg_form.html" # 없으면 모델명_form.html
    form_class = OppkgForm
    
    # 인증되고 스테프나 superuser만 신규등록 가능하고 등록자 기록함
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            form.instance.author = current_user # user를 자동으로 채움
            return super(OppkgCreate, self).form_valid(form)
        else:
            return redirect('books:oppkg_list')

    def get_success_url(self):
        return reverse('books:oppkg_list')

class OppkgAdd(LoginRequiredMixin, CreateView):
    model = Oppkg
    template_name = "books/oppkg_add_form.html"
    form_class = OppkgForm

    def get_context_data(self, **kwargs):
        context = super(OppkgAdd, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = SubsInlineFormSet(self.request.POST)
        else:
            context['formset'] = SubsInlineFormSet(initial=[
                {'year': 1,'num_5gm': 0,'num_4gm': 0,'num_5gf': 0,}
                ])
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            current_user = self.request.user
            if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
                form.instance.author = current_user # user를 자동으로 채움
            else:
                return self.render_to_response(self.get_context_data(form=form))
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return redirect('books:oppkg_list')
        else:
            return self.render_to_response(self.get_context_data(form=form))


class OppkgUpdate(UpdateView):
    model = Oppkg
    form_class = OppkgForm
    template_name = "books/oppkg_update.html" # 헷갈리니 넣어서 분리하자.
    
    # 작성자나 superuser만 업데이트하도록
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and (request.user == self.get_object().author or request.user.is_superuser):
            return super(OppkgUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

    def get_success_url(self):
        return reverse('books:oppkg_list')

def oppkg_delete(request, pk):
    oppkg = get_object_or_404(Oppkg, pk=pk)
    messages.warning(request,"지웠습니다.")
    if request.user.is_authenticated and (request.user == oppkg.author or request.user.is_superuser):
        oppkg.delete()
        return redirect('books:oppkg_list')
    else:
        raise PermissionDenied

# class OppkgDelete(DeleteView):
#     model = Oppkg
#     def get_success_url(self):
#         return reverse('books:oppkg_list')

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
