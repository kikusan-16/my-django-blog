"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'app'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='detail'),
    path('articles/create/', views.ArticleCreateView.as_view(), name='create'),
    path('articles/update/<int:pk>/', views.ArticleUpdateView.as_view(), name='update'),
    path('categories/<str:category_slug>/', views.CategoryArticleView.as_view(), name='category_article'),
    path('tags/<str:tag_slug>/', views.TagArticleView.as_view(), name='tag_article'),
    path('search/', views.SearchArticleView.as_view(), name='search_article'),
    path('markdowntohtml/', views.MarkdownToHtmlView.as_view(), name='markdown_to_html'),
    #path('categories/', views.CategoryListView.as_view()),
    #path('tags/', views.TagListView.as_view()),
]
