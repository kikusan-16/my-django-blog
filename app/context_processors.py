from django.db.models import Count, Q

from .models import Tag, Article


def common(request):
    context = {
        'articles': Article.objects.all()[:5],
        'tags': Tag.objects.annotate(
            num_articles=Count('article', filter=Q(article__is_public=True))),
    }
    return context