from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from adminuser.models import Admin

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

class LoginForm(forms.Form):
	username = forms.CharField(label=(u'User name'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))