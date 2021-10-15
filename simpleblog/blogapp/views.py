from django.http import Http404
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from blogapp.models import Post


class PostListView(ListView):
    model = Post
    template_name = 'blogapp/categories.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blogapp/category_update.html'
    fields = ['title', 'user_post']
    success_url = reverse_lazy('blog:categories')

    def form_valid(self, form):
        form.instance = form.save(commit=False)
        form.instance.user_id = self.request.user
        form.instance.save()
        return super(PostCreateView, self).form_valid(form)


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
