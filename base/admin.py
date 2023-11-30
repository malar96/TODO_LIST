# todo/admin.py
# todo/admin.py
from django.contrib import admin
from .models import Task, Tag

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('timestamp',)
    list_filter = ('status', 'tags')
    fieldsets = (
        ('Task Details', {
            'fields': ('title', 'description', 'due_date', 'tags', 'status'),
        }),
        ('Timestamp Information', {
            'fields': ('timestamp',),
            'classes': ('collapse',),  # Use 'collapse' class to hide by default
        }),
    )
    


admin.site.register(Task,TaskAdmin)
admin.site.register(Tag)
