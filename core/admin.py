from django.contrib import admin
from .models import Blog
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    list_filter = ('title', 'content')
    search_fields = ('title', 'content')
    ordering = ['title']
    fieldsets = (
        (None, {
            'fields': ('title', 'content')
        }),
    )
    def __str__(self):
        return self.title
