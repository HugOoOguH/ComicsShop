from django.contrib import admin
from .models import Category, SuperHero, Comic, Company

class CompanyAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class SuperHeroAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('name',)}

class ComicAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug':('title',)}


admin.site.register(Category, CategoryAdmin,)
admin.site.register(SuperHero, SuperHeroAdmin,)
admin.site.register(Comic, ComicAdmin,)
admin.site.register(Company, CompanyAdmin,)

# Register your models here.
