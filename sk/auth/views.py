from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from auth.models import SignupForm
from sooouk.models import *


@login_required
def login_redirect(request):
	return render_to_response('sooouk/passport.html', context_instance=RequestContext(request))

def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

def sign_up(request):
	def errorHandle(error):
		form = SignupForm()
		return render_to_response(
			'registration/signup.html',{
			'error':error,
			'form': form,
		}, context_instance=RequestContext(request))
	#check for post data
	if request.method == 'POST':
		new_user = request.POST.copy()
		error = "Doesn't have the keys user and/or password."
		#check to see there are values
		if new_user.has_key('username') and new_user.has_key('password') and new_user.has_key('email') and new_user['username'] and new_user['password'] and new_user['email']:
			#make sure the username is not already taken
			try:
				a = User.objects.get(username=new_user['username'])
			except:
			
				#make sure the email not in use
				try:
					a = User.objects.get(email=new_user['email'])
				except:
					user = User.objects.create_user(new_user['username'], new_user['email'], new_user['password'])
					user.save()
					user = authenticate(username=new_user['username'], password=new_user['password'])
					if user is not None:
						if user.is_active:
							login(request, user)
							#for now it is going to redirect back to the home page, but in the future it should redirect back to the page that you clicked sign in from
							#or maybe link to where they can fill out their profile
							print "redirecting to the landing page"
							return HttpResponseRedirect(reverse('soooukAlpha.views.landing'))
						else:
							error = "Your account has been disabled."
					else:
						error = "Username and/or password were incorrect."					
				else:
					error = "This Email address is being used."
			else:
				error = "This Username is currently taken."
		return errorHandle(error)
	else:
		form = SignupForm()
		return render_to_response('registration/signup.html',{
			'form': form,
		},context_instance=RequestContext(request))
	
	
	
	
	
	
	
	
	
	
	
	
	
	