from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

"""
Admin class is a basic user, with a ForeignKey mapping to the Django User
it inherits its information from. It also has a name.

Technically unecessary at this time, because Django's User object has a FirstName and
LastName field, but this model was created for expansion, in case any other
information was needed later.
"""
class Admin(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=140)

	def __str__(self):
		return self.name

#create user object to attach to admin object
def create_admin_user_callback(sender, instance, **kwargs):
	admin, new = Admin.objects.get_or_create(user=instance)
post_save.connect(create_admin_user_callback, User)