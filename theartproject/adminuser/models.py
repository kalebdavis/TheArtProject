from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Admin(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=140)

	def __str__(self):
		return self.name

#create user object to attach to admin object
def create_admin_user_callback(sender, instance, **kwargs):
	admin, new = Admin.objects.get_or_create(user=instance)
post_save.connect(create_admin_user_callback, User)