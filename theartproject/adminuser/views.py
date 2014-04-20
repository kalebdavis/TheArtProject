from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from adminuser.forms import RegistrationForm, LoginForm

#will be limited to only people with certain password
def registerAdmin(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		#runs through clean data methods in forms.py
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
			user.save()
			#provided by AUTH_PROFILE_MODULE in settings.py
			admin = user.get_profile()
			admin.name = form.cleaned_data['name']
			admin.save()
			return HttpResponseRedirect('/profile/')
		else:
			return render_to_response('register_admin.html', {'form':form}, context_instance=RequestContext(request))
	else:
		'''user is not submitting form, show a blank registration form'''
		form = RegistrationForm()
		context = {'form':form}
		return render_to_response('register_admin.html', context, context_instance=RequestContext(request))

def requestLogin(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/profile/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			#built in Django user authentication
			admin = authenticate(username=username, password=password)
			if admin is not None:
				login(request, admin)
				return HttpResponseRedirect('/profile/')
			else:
				return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))
	else:
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context, context_instance=RequestContext(request))

def requestLogout(request):
	logout(request)
	return HttpResponseRedirect('/')