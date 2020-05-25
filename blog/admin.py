from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "published_at")
    raw_id_fields = ("author", "likes", "tags", )
    date_hierarchy = 'published_at'


class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "text", "post", "published_at",)
    list_display_links = None
    raw_id_fields = ("post", "author",)


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)