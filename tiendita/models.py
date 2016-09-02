from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# 
class Company(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='companies')
	description = models.TextField()
	slug = models.SlugField(max_length=150)

	def __str__(self):
		return self.name

class SuperHero(models.Model):
	company = models.ForeignKey(Company, related_name='companyH', blank=True, null=True)
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='superheroes')
	history = models.TextField()
	number = models.IntegerField()
	slug = models.SlugField(max_length=150)

	def __str__(self):
		return self.name

class Category(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	slug = models.SlugField(max_length=150)

	def __str__(self):
		return self.name

class Comic(models.Model):
	# company = models.ForeignKey(Company, related_name="companyC")
	superhero = models.ForeignKey(SuperHero, related_name="superheroC")
	category = models.ManyToManyField(Category, related_name="categoryC")
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to='comics')
	synopsis = models.TextField()
	slug = models.SlugField(max_length=250)
	price = models.FloatField()
	start_date = models.DateField(auto_now=True)

	def __str__(self):
		return self.title

