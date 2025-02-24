from django.contrib import admin
from blog.models import Comment, Like, Blog, BlogMedia

class BlogMediaInline(admin.TabularInline):
    model = BlogMedia
    extra = 1

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogMediaInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'comment', 'blog', 'created_at')
    

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'blog', 'created_at')
