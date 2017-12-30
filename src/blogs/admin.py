from django.contrib import admin



from blogs.models import Blog, Category, Post

admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Post)


