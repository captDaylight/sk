from sooouk.models import *
from random import randrange
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.translation import ungettext
from sooouk.models import *
import json

def createUsersItems():
	counter = 0
	user = User.objects.get(id=1)
	post = 'Andouille turkey pastrami shank ribeye. Short loin biltong corned beef, sirloin ribeye pork belly bresaola swine pancetta bacon ground round kielbasa hamburger. Meatloaf pork chop sirloin, bacon pork loin jerky turducken corned beef pancetta frankfurter prosciutto. Pork belly sausage turducken salami meatloaf brisket andouille, sirloin ground round tenderloin jowl chicken t-bone pancetta. Jowl biltong hamburger prosciutto ground round. Ham bacon ball tip ground round swine bresaola, salami rump. Jerky sausage meatloaf prosciutto sirloin short ribs.'
	words = ['boat', 'balloons', 'building', 'cardboard','wallet', 'cats', 'cup', 'bag', 'tattly', 'umbrella', 'art', 'gold', 'golf', 'cloud','goldfish','food']
	local = ['france','spain','bolivia','china','japan', 'india', 'uganda','botswana']
	imgurls = ['http://img.ffffound.com/static-data/assets/6/6845e7100126621f664449d1119da699c65ed99e_m.jpg','http://img.ffffound.com/static-data/assets/6/3bd80bf3b4d30e9590788742e43da03b988b6033_m.jpg', 'http://img.ffffound.com/static-data/assets/6/a3e53bf7bb85d14097236b528f7c5c1db1ef28ca_m.jpg', 'http://img.ffffound.com/static-data/assets/6/750b1f614210c99b705f817bc5685b45b4bbb064_m.jpg', 'http://img.ffffound.com/static-data/assets/6/a27198a8ab6253fe6997b95168e9d829b2183a1a_m.jpg','http://img.ffffound.com/static-data/assets/6/7226ee1e7d238d66c63eee7de191a1b8b2b252be_m.jpg', 'https://fbcdn-sphotos-a.akamaihd.net/hphotos-ak-snc6/217655_1920066292024_1553056560_2056419_3990564_n.jpg', 'http://img.ffffound.com/static-data/assets/6/87d0da9c653b892d4eaa9315082dee102ba1fb61_m.jpg']
	product_type = ['Food','Clothing', 'Beauty', 'Household', 'Recreation', 'Drink']
 	while counter < 200:
		i = Item()
		title = words[randrange(0,len(words))] + ' ' + words[randrange(0,len(words))]
		i = user.get_profile().item_set.create(title=title,item_size = randrange(1,4), post=post,location=local[randrange(0,len(local))], photourl = imgurls[randrange(0,len(imgurls))], product_type= product_type[randrange(0,len(product_type))])
		counter += 1