from django.contrib import admin

from .models import Gallery, Notice, messages, projects

# Register your models here.

admin.site.register(Gallery)
admin.site.register(Notice)
admin.site.register(projects)
admin.site.register(messages)
