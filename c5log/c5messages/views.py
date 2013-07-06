import datetime
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.http import Http404
from django.db.models import Count, Avg
from braces.views import LoginRequiredMixin
from c5messages.models import MessageLog, DailyActivity


class HomeView(LoginRequiredMixin, TemplateView):

	template_name = "home.html"

	def get_context_data(self, **kwargs):
		context = super(HomeView, self).get_context_data(**kwargs)
		context['msgs'] = MessageLog.objects.order_by('-logtime').all()[:25]
		context['earliest_date'] = MessageLog.objects.order_by('logtime').values('logtime')[0]['logtime']
		context['msg_count'] = MessageLog.objects.count()
		return context


class ArchiveView(LoginRequiredMixin, ListView):

	model = MessageLog
	context_object_name = "msgs"
	template_name = "archives.html"

	def get_queryset(self, **kwargs):
		self.archive_date = datetime.datetime.utcnow()
		self.earliest_date = MessageLog.objects.order_by('logtime').values('logtime')[0]['logtime']
		
		try:
			if self.request.GET.get('log_date'):
				self.archive_date = datetime.datetime.strptime(self.request.GET.get('log_date'), '%m-%d-%Y')
			elif self.kwargs.get('log_date'):
				self.archive_date = datetime.datetime.strptime(self.kwargs.get('log_date'), '%m-%d-%Y')

			return MessageLog.objects.filter(logtime__day=self.archive_date.day, logtime__month=self.archive_date.month, logtime__year=self.archive_date.year)
		except:
			raise Http404

	def get_context_data(self, **kwargs):
		context = super(ArchiveView, self).get_context_data(**kwargs)
		today = datetime.datetime.utcnow()
		context['archive_date'] = self.archive_date
		context['earliest_date'] = self.earliest_date

		if self.archive_date.date() > self.earliest_date.date():
			context['prev_date'] = self.archive_date - datetime.timedelta(days=1)
		if self.archive_date.date() < today.date():
			context['next_date'] = self.archive_date + datetime.timedelta(days=1)
		return context


class SearchView(LoginRequiredMixin, ListView):

	model = MessageLog
	context_object_name = "msgs"
	template_name = "search.html"
	paginate_by = 50

	def get_queryset(self, **kwargs):
		if self.request.GET.get('q'):
			search = self.request.GET.get('q').strip()
			return MessageLog.objects.filter(message__icontains=search)
		else:
			raise Http404

	def get_context_data(self, **kwargs):
		context = super(SearchView, self).get_context_data(**kwargs)
		if self.kwargs.get('page'):
			context['page'] = self.kwargs.get('page')
		else:
			context['page'] = 1
		context['q'] = self.request.GET.get('q').strip()

		return context


class StatsView(LoginRequiredMixin, TemplateView):

	template_name = "stats.html"

	def get_context_data(self, **kwargs):
		context = super(StatsView, self).get_context_data(**kwargs)
		context['top_users'] = MessageLog.objects.values('user').annotate(msg_count=Count('user')).order_by('-msg_count').filter(msg_count__gt=1)[:10]
		context['daily_activity'] = DailyActivity.objects.all()
		context['total_msgs'] = MessageLog.objects.count()
		context['unique_users'] = MessageLog.objects.all().values('user').distinct().count()
		return context
