from django.contrib import admin

from beaches.models import Category, Page, UserProfiles

class CategoryAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('name',)}

admin.site.register(Category)
admin.site.register(Page)
admin.site.register(UserProfiles)
