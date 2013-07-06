from django.contrib import admin
from c5messages.models import MessageLog

class MessageLogAdmin(admin.ModelAdmin):
	list_display = ('logtime', 'user', 'message')
	list_filter = ['logtime']
	search_fields = ['user', 'message']


admin.site.register(MessageLog, MessageLogAdmin)