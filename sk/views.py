from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from sooouk.models import *
import json


def landing(request):
	following_list = []
	latest_item_list = Item.objects.all().order_by('-created_at')[:50]
	if request.user.is_authenticated():
		following_list = request.user.get_profile().following.all()[:50]
	return render_to_response('sooouk/index.html', {'latest_item_list': latest_item_list, 'following_list': following_list},context_instance=RequestContext(request))
	
# there are three situations being passed for following and vote
# 1 = user logged in and NOT following the item/user.
# 2 = user logged in and following the item/user.
# 3 = user NOT logged in
# in the case that the logged in user uploaded the product, the template will handle the issue
def item(request, item_id):
	i = get_object_or_404(Item, pk=item_id)
	if request.user.is_authenticated():
		try:
			v = Vote.objects.get(item=i, voter=request.user.get_profile())
			hv = True
		except:
			hv = False	
		following_list = request.user.get_profile().following.all()[:50]
		try:
			request.user.get_profile().following.get(id=i.user.user.id)
		except:
			f = 1
		else:
			f = 2
		return render_to_response('sooouk/item.html', {'item': i, 'isFollowing': f,'has_voted':hv,'following_list': following_list}, context_instance=RequestContext(request))
	else:
		f = 3
	return render_to_response('sooouk/item.html', {'item': i}, context_instance=RequestContext(request))
	
	
	

@login_required
def upload(request):
	#return render_to_response('sooouk/upload.html', context_instance=RequestContext(request))
	def errorHandle(error):
		form = UploadForm()
		return render_to_response(
			'sooouk/upload.html',{
			'error':error,
			'form': form,
		}, context_instance=RequestContext(request))
	#check for post data
	if request.user.is_authenticated():
		following_list = request.user.get_profile().following.all()[:50]
	if request.method == 'POST':
		new_item = request.POST.copy()
		error = "No information was sent."
		#check to see there are values
		if new_item.has_key('title') and new_item.has_key('post') and new_item.has_key('location') and new_item.has_key('photourl') and new_item['title'] and new_item['post'] and new_item['location'] and new_item['photourl']:
			#see if the product has a duplicate title
			try:
				i = Item.objects.get(title=new_item['title'])
			except:
				i = request.user.get_profile().item_set.create(title=new_item['title'], post=new_item['post'],location=new_item['location'], photourl = new_item['photourl'])
				i.save()	
				print "the item was saved"
			else:
				error = "There is already another product with this title."
		return errorHandle(error)

	else:
		form = UploadForm()
		return render_to_response('sooouk/upload.html',{
			'form': form,
			'following_list': following_list,
		},context_instance=RequestContext(request))
	
	
@login_required
def vote(request, item_id, user_id):
	if request.method == 'GET':
		u = User.objects.get(id=user_id)
		i = Item.objects.get(id=item_id)
		Vote.objects.get_or_create(item=i, voter=u.get_profile())
		success = ungettext(
	        '%(count)d Vote',
	        '%(count)d Votes',
	    count) % {
	        'count': Vote.objects.count(),
	    }
		success = {"success": success}
	else:
		success = {"success": "NOT A SUCCESS"}
	return HttpResponse(json.dumps(success), mimetype="application/javascript")	

	
@login_required
def follow(request, user_id):
	if request.method == 'GET':
		u = User.objects.get(pk=user_id)
		u.get_profile().followers.add(request.user.get_profile())
		print u.get_profile().followers.all()		
	success = {"success": "it was a success"}
	print success
	return HttpResponse(json.dumps(success), mimetype="application/javascript")

@login_required
def unfollow(request, user_id):
	if request.method == 'GET':
		u = User.objects.get(pk=user_id)
		u.get_profile().followers.remove(request.user.get_profile())
		print u.get_profile().followers.all()
	success = {"success": "it was a success"}
	print success
 	return HttpResponse(json.dumps(success), mimetype="application/javascript")





@login_required
def passport(request, user_id):
	#return render_to_response('sooouk/upload.html', context_instance=RequestContext(request))
	def errorHandle(error):
		form = UploadForm()
		return render_to_response(
			'sooouk/passport.html',{
			'error':error,
			'form': form,
		}, context_instance=RequestContext(request))
	#check for post data
	
	item_list = []
	item_list = Item.objects.filter(user=request.user.get_profile())[:50]
	item_vote_list = []
	item_vote_list = Item.objects.filter()[:50]
	profile = User.objects.get(id=user_id)
	following_list = []
	if request.user.is_authenticated():
		following_list = request.user.get_profile().following.all()[:50]
	profile_followers_list = profile.get_profile().followers.all()[:50]
	profile_following_list = profile.get_profile().following.all()[:50]
	if request.method == 'POST':
		error = "No information was sent."
		#check to see there are values
		if request.POST.has_key('first_name') and request.POST.has_key('last_name') and request.POST.has_key('about_me') and request.POST['first_name'] and request.POST['last_name'] and request.POST['about_me']:
			#see if the product has a duplicate title
			try:
				u = request.user
				print 
				u.first_name = request.POST['first_name']
				u.last_name = request.POST['last_name']
				u.get_profile().about_me = request.POST['about_me']
				u.save()
				return HttpResponseRedirect(reverse(passport))			
			except:
				error = "There is already another product with this title."
		return errorHandle(error)

	else:
		form = PassportForm()
		return render_to_response('sooouk/passport.html',{
			'form': form,
			'profile': profile.get_profile(),
			'following_list': following_list,
			'profile_followers_list': profile_followers_list,
			'profile_following_list': profile_following_list,
			'item_vote_list':item_vote_list,
			'item_list': item_list,
		},context_instance=RequestContext(request))
	
