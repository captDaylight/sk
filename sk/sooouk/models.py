from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django import forms

	
class UserProfile(models.Model):
	user = models.OneToOneField(User)
	about_me = models.TextField()
	followers = models.ManyToManyField("self", null=True, symmetrical=False, related_name="following")
	created_at = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return self.user.username	

#EXTENDING THE USER PROFILE
def create_user_profile(sender, instance, created, **kwargs):  
    if created:  
       profile, created = UserProfile.objects.get_or_create(user=instance)  

post_save.connect(create_user_profile, sender=User) 

class CategoryType(models.Model):
	category = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	def __unicode__(self):
		return self.title	

# class CategoryItem(models.Model):
# 	category = models.CharField(max_length = 100)
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	def __unicode__(self):
# 		return self.title
		
class Item(models.Model):
	user = models.ForeignKey(UserProfile)
	title = models.CharField(max_length = 128)
	post = models.TextField()
	photourl = models.CharField(max_length = 500)
	location = models.CharField(max_length = 200)
	#convert location on redirect to item full page after creation 
	latitude = models.CharField(max_length = 100)
	longitude = models.CharField(max_length = 100)
	country = models.CharField(max_length = 100)
	product_type = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	item_size = models.IntegerField();
	def __unicode__(self):
		return self.title

class Vote(models.Model):
	item = models.ForeignKey(Item)
	voter = models.ForeignKey(UserProfile)
	def __unicode__(self):
		return self.item.title

class UploadForm(forms.Form):
	#category_choices = [(m.id, m.category) for c in Categories.objects.all()]
	title = forms.CharField(max_length = 100)
	post = forms.CharField(widget=forms.Textarea)
	location = forms.CharField(max_length = 200)
	photourl = forms.CharField(max_length = 500)
    #categories = forms.MultipleChoiceField(required=True, label='Item Category', choices=maintainer_choices)
	
	
class PassportForm(forms.Form):
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	about_me = forms.CharField(widget=forms.Textarea)		
