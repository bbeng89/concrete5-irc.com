from django.db import models


class MessageLog(models.Model):
	logtime = models.DateTimeField(auto_now_add=True)
	user = models.CharField(max_length=50)
	message = models.CharField(max_length=512)

	def __unicode__(self):
		return u"%s|<%s> %s" % (self.logtime, self.user, self.message[:25])


class DailyActivity(models.Model):
	day_of_week = models.CharField(db_column='day_of_week', max_length=9)
	day_num = models.IntegerField(primary_key=True)
	average_msgs = models.DecimalField(max_digits=24, decimal_places=4)

	class Meta:
		db_table = 'vw_day_avgs'
		managed = False
