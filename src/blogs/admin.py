from django.contrib import admin



from blogs.models import Blog, Category, Post


admin.site.register(Category)



admin.site.site_header= "WORDPLEASE ADMIN"
admin.site.site_title= admin.site.site_header


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'summary', 'published_at')
    list_filter = ('user','title', 'category', 'published_at')
    search_fields = ('title', 'summary','body' 'category')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('user','name','url')
    list_filter = ('user','name', 'url')
    search_fields = ('name', 'description','url')
