from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from app.models import Article

class BlogArticleSitemap(Sitemap):
    changefreq = "never"
    priority = 0.8

    def items(self):
        return Article.objects.filter(is_public=True)

    def location(self, obj):
        return reverse('app:detail', args=[obj.pk])
    
    def lastmod(self, obj):
        return obj.published_at