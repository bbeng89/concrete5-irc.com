from django.db import models

# Create your models here.

class SystemLog(models.Model):
	logtime = models.DateTimeField(auto_now_add=True)
	message = models.CharField(max_length=1000)

	def __unicode__(self):
		return u"<%s> %s" % (self.logtime, self.message[:25])
