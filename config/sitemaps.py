from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from app.models import Article, Category, Tag

class BlogArticleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return Article.objects.filter(is_public=True)

    def location(self, obj):
        return reverse('app:detail', args=[obj.pk])
    
    def lastmod(self, obj):
        return obj.published_at


class BlogCategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Category.objects.all()

    def location(self, obj):
        return reverse('app:category_article', args=[obj.category_slug])


class BlogTagSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Tag.objects.all()

    def location(self, obj):
        return reverse('app:tag_article', args=[obj.tag_slug])


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['app:index','app:article_list']

    def location(self, item):
        return reverse(item)