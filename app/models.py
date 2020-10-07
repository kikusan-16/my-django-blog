from django.db import models
from django.utils import timezone

import markdown
import os

class Category(models.Model):

    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Article(models.Model):

    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    is_public = models.BooleanField(default=False)

    def markdown_to_html(self):
        """Markdown を HTML に変換して出力
        さらに拡張機能を使用して目次を自動生成する"""
        md = markdown.Markdown(
            extensions=['extra', 'admonition', 'sane_lists', 'toc'])
        html = md.convert(self.content)
        return html

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Media(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', verbose_name='添付ファイル')

    def __str__(self):
        return self.name

    def get_filename(self):
        return os.path.basename(self.image.name)