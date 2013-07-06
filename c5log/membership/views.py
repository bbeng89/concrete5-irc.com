from django.core.urlresolvers import reverse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout


class LoginView(View):

	def get(self, request, *args, **kwargs):
		return render(request, 'login.html')

	def post(self, request, *args, **kwargs):
		email = request.POST.get('email')
		password = request.POST.get('password')
		error_msg = 'Invalid email/password combination entered'

		user = authenticate(username=email, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return redirect('home')
			else:
				if request.GET.get('reg'):
					reg_code = request.GET.get('reg')
					if user.reg_code == reg_code:
						user.is_active = True
						user.save()
						login(request, user)
						return redirect('home')
					else:
						error_msg = 'An error occurred activating your account. Please contact admin@concrete5-irc.com'
				else:
					error_msg = 'Your account is inactive. If you have not yet activated your account please check your email to complete your registration.'

		return render(request, 'login.html', {'error': error_msg})


def logout_user(request):
	response = logout(request, next_page=reverse('login'))
	return response