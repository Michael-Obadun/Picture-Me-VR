from django.contrib import admin
from .models import Post, Comment, Meeting
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug','author')
    search_fields = ['title']
    list_filter = ('banner',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)



# Register your models here.
admin.site.register(Comment)
admin.site.register(Meeting)



