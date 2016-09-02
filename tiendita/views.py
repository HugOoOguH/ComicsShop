from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.views.generic import View
from .models import Company, Comic
# Create your views here.


class CompaniesListView(View):
	def get(self,request):
		template_name = "tiendita/list_company.html"
		company = Company.objects.all()
		context = {
		'company':company,
		}
		return render(request,template_name,context)

class ComicsListView(View):
	def get(self, request, id):
		template_name = "tiendita/categories.html"
		company = get_object_or_404(Company, id=id)
		comics = Comic.objects.all().filter(company=company)
		context = {
		'comics':comics,
		}
		return render(request, template_name, context)



class ProductDetailView(View):
	pass