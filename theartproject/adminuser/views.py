"""
adminuser views control the logging in, logging out, registering of an admin, as
well as any other functionality the admins need to have in the future.
"""
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from adminuser.forms import RegistrationForm, LoginForm

#will be limited to only people with certain password
"""
registerAdmin uses the RegistrationForm from adminuser/forms.py, cleans the information
entered in there, and creates a User object as well as an admin object.

Checks the validation of the form, and redirects the user once the process is complete.
"""
def registerAdmin(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/admin_home/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		#runs through clean data methods in forms.py
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
			user.groups.add(Group.objects.get(name='admin'))
			user.save()
			#provided by AUTH_PROFILE_MODULE in settings.py
			admin = user.get_profile()
			admin.name = form.cleaned_data['name']
			admin.save()
			return HttpResponseRedirect('/admin_home/')
		else:
			return render_to_response('register_admin.html', {'form':form}, context_instance=RequestContext(request))
	else:
		'''user is not submitting form, show a blank registration form'''
		form = RegistrationForm()
		context = {'form':form}
		return render_to_response('register_admin.html', context, context_instance=RequestContext(request))


"""
requestLogin uses the Django user authentication methods to request logging in.

If the user is already logged in, they are redirected.

Otherwise, Django's methods authenticate and login are called.
"""
def requestLogin(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/admin_home/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			#built in Django user authentication
			admin = authenticate(username=username, password=password)
			if admin is not None:
				login(request, admin)
				return HttpResponseRedirect('/admin_home/')
			else:
				return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
	else:
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context, context_instance=RequestContext(request))

"""
requestLogout uses Django's logout method to log out the user

Redirects to the home page
"""
def requestLogout(request):
	logout(request)
	return HttpResponseRedirect('/')

"""
viewHomePage is adminuser's redirection to their dashboard, where the admin can then
add and remove products and all other admin functionality.

This method checks to make sure that there is a user logged in and that the user
is an admin.
"""
def viewHomePage(request):
	if request.user.is_authenticated():
		print(request.user)
		print(Group.objects.get(name="admin").user_set.all())
		if request.user in Group.objects.get(name="admin").user_set.all():
			return render_to_response('admin_home.html', locals(), context_instance=RequestContext(request))
	return HttpResponseRedirect('/')