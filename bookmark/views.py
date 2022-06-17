from django.shortcuts import render

from .models import Bookmark        #Bookmark에서 models를 가져온다

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView

class BookmarkList(ListView):
    model = Bookmark

class BookmarkCreate(CreateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_create'
    success_url = '/'

class BookmarkUpdate(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url', 'contents']
    template_name_suffix = '_update'
    success_url = '/'

class BookmarkDelete(DeleteView):
    model = Bookmark
    template_name_suffix = '_delete'
    success_url = '/'

class BookmarkDetail(DetailView):
    model = Bookmark
    template_name = 'bookmark/bookmark_detail.html'
