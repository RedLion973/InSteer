from django.contrib import admin
from InSteer.ownership.models import DeliveredDocument, Project, ProjectActor, ProjectDeliveredDocument, ProjectRole, ProjectStep, Step, Task
from InSteer.ownership.forms import ProjectActorForm
    
class ProjectActorAdmin(admin.ModelAdmin):
    form = ProjectActorForm
    list_display = ['human_readable_name', 'type', 'project', 'get_full_roles',]
    list_filter = ['project', 'type',]
    search_fields = ['user__fist_name', 'user__last_name',]

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['name','description','year'], 'classes': ['wide']}),
        ('CRM',                 {'fields': ['client']}),
    ]
    list_display = ['name', 'client', 'year',]
    list_filter = ['client',]
    search_fields = ['name', 'client',]

admin.site.register(DeliveredDocument)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectActor, ProjectActorAdmin)
admin.site.register(ProjectRole)
admin.site.register(ProjectStep)
admin.site.register(Task)
admin.site.register(Step)
admin.site.register(ProjectDeliveredDocument)