from django.contrib import admin
from .models import ChildProfile, Content, ActivityLog

admin.site.register(ChildProfile)
admin.site.register(Content)
admin.site.register(ActivityLog)
