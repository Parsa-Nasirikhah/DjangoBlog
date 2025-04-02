from django.contrib import admin
from .models import Post,Comment,Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_title', 'publish_date']
    list_display_links = ['id', 'post_title']
    list_filter = ['publish_date']
    search_fields = ['post_title']


admin.site.register(Comment)
admin.site.register(Tag)

# admin.site.register(Post, PostAdmin)
