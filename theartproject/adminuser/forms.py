from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from adminuser.models import Admin

"""
RegistrationForm allows for the registration of any user.

Sets up form fields for username, email, password, and a second password for verification.
Overrides the clean method for clean_username to check if the username is already in the database.

TODO: Ask for another password to get into the registration page, so only Art House members with permission
can create admin users. This setup automatically gives the users admin permission, so this should be 
password protected.
"""
class RegistrationForm(ModelForm):
	username = forms.CharField(label=(u'User name'))
	email = forms.EmailField(label=(u'Email address'))
	#widget makes char field into password field
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(label=(u'Verify password'), widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = Admin
		exclude = ('user',)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is already taken.")

	def clean(self):
		if self.cleaned_data['password'] != self.cleaned_data['password1']:
			raise forms.ValidationError("The passwords do not match, try again.")
		return self.cleaned_data

"""
LoginForm takes the user's information to authenticate the user and log in.
"""
class LoginForm(forms.Form):
	username = forms.CharField(label=(u'User name'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))