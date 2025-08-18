from django.contrib import admin
from .models import Skill, Project, Achievement

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'project_type', 'github_link')
    list_filter = ('project_type', 'skills')
    search_fields = ('title', 'resume_description')
    
    def github_link(self, obj):
        return f'<a href="{obj.github_url}" target="_blank">View</a>'
    github_link.allow_tags = True

admin.site.register(Skill)
admin.site.register(Achievement)