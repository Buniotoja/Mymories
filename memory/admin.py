from django.contrib import admin

from memory.models import Memory, Post


@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'memory_type', 'id']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'date']
    list_filter = ['memory_id']