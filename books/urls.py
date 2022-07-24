from django.urls import path
from . import views


app_name = 'books'
urlpatterns = [
    path('nf/', views.NfListView.as_view(), name="nf_list"),
    path('nf/<int:pk>/', views.NfDetailView.as_view(), name="nf_detail"),
    path('nf/new', views.NfCreateView.as_view(), name='nf_new'),
    path('nf/<int:pk>/update', views.NfUpdateView.as_view(), name='nf_update'),
    path('nf/<int:pk>/delete', views.NfDeleteView.as_view(), name='nf_delete'),

    path('oppkg/', views.OppkgList.as_view(), name="oppkg_list"),
    path('oppkg/<int:pk>/', views.OppkgDetail.as_view(), name="oppkg_detail"),
    path('oppkg/create', views.OppkgCreate.as_view(), name='oppkg_create'),
    path('oppkg/<int:pk>/update', views.OppkgUpdate.as_view(), name='oppkg_update'),
    path('oppkg/<int:pk>/delete', views.OppkgDelete.as_view(), name='oppkg_delete'),

    path('subs/', views.SubsList.as_view(), name="subs_list"),
    path('subs/<int:pk>/', views.SubsDetail.as_view(), name="subs_detail"),
    path('subs/create', views.SubsCreate.as_view(), name='subs_create'),
    path('subs/<int:pk>/update', views.SubsUpdate.as_view(), name='subs_update'),
    path('subs/<int:pk>/delete', views.SubsDelete.as_view(), name='subs_delete'),

    # /books/
    path('', views.BooksModelView.as_view(), name='index'),

    # /books/book/
    path('book/', views.BookList.as_view(), name='book_list'),

    # /books/author/
    path('author/', views.AuthorList.as_view(), name='author_list'),

    # /books/publisher/
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),

    # /books/book/99/
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),

    # /books/author/99/
    path('author/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),

    # /books/publisher/99/
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisher_detail'),
]