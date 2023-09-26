from django.contrib import admin
from .models import Post, Comment, Tag


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','is_public','message','message_length','created_at']
    list_display_links = ['message']
    list_filter = ['created_at','is_public']
    search_fields = ['message']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
