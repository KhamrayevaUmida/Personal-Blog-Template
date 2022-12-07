from django.contrib import admin
from .models import Post
from .models import TopPost, NextPost

# admin.site.register(Post)

# admin.site.register(TopPost)


@admin.register(Post)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'date', 'tanlov')

@admin.register(TopPost)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'date', 'tanlov')

@admin.register(NextPost)
class ArticlePost(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'date', 'tanlov', 'content',)