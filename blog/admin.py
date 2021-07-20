from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'short_description', 'time_create', 'is_published')
    list_display_links = ('title',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}
