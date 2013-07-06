from django.contrib import admin
from system.models import SystemLog

class SystemLogAdmin(admin.ModelAdmin):
	list_display = ('logtime', 'message')
	list_filter = ['logtime']
	search_fields = ['message']


admin.site.register(SystemLog, SystemLogAdmin)