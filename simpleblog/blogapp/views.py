from django.contrib.auth.decorators import user_passes_test
from django.http import request, HttpResponseForbidden, Http404, HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse, reverse_lazy
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from blogapp.models import Post

from blogapp.forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = 'blogapp/categories.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blogapp/category_update.html'
    success_url = reverse_lazy('blog:categories')


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'blogapp/category_update.html'
    success_url = reverse_lazy('blog:categories')
    fields = ['title', 'user_post']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Статьи/редактирование'
        return context

    def get_object(self, queryset=None):
        obj = super(PostUpdateView, self).get_object()
        if not obj.user_id == self.request.user:
            raise Http404
        return obj


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blogapp/category_delete.html'
    success_url = reverse_lazy('blog:categories')

    def get_object(self, queryset=None):
        obj = super(PostDeleteView, self).get_object()
        if not obj.user_id == self.request.user:
            raise Http404
        return obj
