from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content', )


# Register your models here.
admin.site.register(Post, PostAdmin)