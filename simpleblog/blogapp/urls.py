from django.urls import path
import blogapp.views as blogapp

app_name = 'blog'

urlpatterns = [
    path('categories/create/', blogapp.PostCreateView.as_view(), name='category_create'),
    path('categories/read/', blogapp.PostListView.as_view(), name='categories'),
    path('categories/update/<int:pk>/', blogapp.PostUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', blogapp.PostDeleteView.as_view(), name='category_delete'),
]
