from django.contrib import admin
from .models import *


class IndexAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo']


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'photo', 'content', 'created_at', 'index']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'published', 'created_at']
    list_filter = ['published', 'created_at']
    search_fields = ['name']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Index, IndexAdmin)
admin.site.register(Portfolio, PortfolioAdmin)




