from django.shortcuts import render
from django.db.models import Count, Q
from django.http import Http404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from .models import Article, Category, Tag


class IndexView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        doc_slug = 'documentation'
        self.category = get_object_or_404(Category, slug=doc_slug)
        context = super().get_context_data(**kwargs)
        context['object_list'] = Article.objects.filter(category=self.category)
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'app/detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        if not obj.is_public and not self.request.user.is_authenticated:
            raise Http404
        return obj


class ArticleListView(ListView):
    paginate_by = 10
    model = Article
    template_name = 'app/article_list.html'


# class CategoryListView(ListView):
#     queryset = Category.objects.annotate(
#         num_articles=Count('article', filter=Q(article__is_public=True)))
#     template_name = 'app/category_list.html'
#
#
# class TagListView(ListView):
#     queryset = Tag.objects.annotate(num_articles=Count(
#         'article', filter=Q(article__is_public=True)))
#     template_name = 'app/tag_list.html'


class CategoryArticleView(ListView):
    paginate_by = 10
    model = Article
    template_name = 'app/category_article_list.html'

    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        self.category = get_object_or_404(Category, slug=category_slug)
        qs = super().get_queryset().filter(category=self.category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context


class TagArticleView(ListView):
    paginate_by = 10
    model = Article
    template_name = 'app/tag_article.html'

    def get_queryset(self):
        tag_slug = self.kwargs['tag_slug']
        self.tag = get_object_or_404(Tag, slug=tag_slug)
        qs = super().get_queryset().filter(tags=self.tag)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

class SearchArticleView(ListView):
    model = Article
    template_name = 'app/search_article.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        lookups = (
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(category__name__icontains=query) |
            Q(tags__name__icontains=query)
        )
        if query is not None:
            qs = super().get_queryset().filter(lookups).distinct()
            return qs
        qs = super().get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context