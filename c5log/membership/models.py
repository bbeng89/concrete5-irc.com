from datetime import datetime
import random, string
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, UserManager


class MemberManager(BaseUserManager):
	def create_user(self, email=None, password=None, **extra_fields):
		now = datetime.utcnow()
		if not email:
			raise ValueError('Email address must be given')
		email = UserManager.normalize_email(email)
		user = self.model(email=email, is_staff=False, is_active=False, is_superuser=False, last_login=now, reg_code=self.create_reg_code(), **extra_fields)
 
		user.set_password(password)
		user.save(using=self._db)
		return user
 
	def create_superuser(self, email, password, **extra_fields):
		u = self.create_user(email, password, **extra_fields)
		u.is_staff = True
		u.is_active = True
		u.is_superuser = True
		u.save(using=self._db)
		return u

	def create_reg_code(self):
		code = ''.join(random.choice(string.ascii_uppercase + string.digits) for r in range(8))
		while(self.model.objects.filter(reg_code=code).count() > 0):
			code = ''.join(random.choice(string.ascii_uppercase + string.digits) for r in range(8))
		return code


class Member(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField('email address', max_length=254, unique=True)
	nick = models.CharField(max_length=16)
	reg_code = models.CharField(max_length=10)
	is_staff = models.BooleanField('staff status', default=False, help_text='Designates whether the user can log into this admin site.')
	is_active = models.BooleanField('active', default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
 	USERNAME_FIELD = 'email'
	objects = MemberManager()

	def get_full_name(self):
		return self.email
 
	def get_short_name(self):
		return self.nick