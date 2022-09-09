from django.contrib import admin
from app.models import LinkData , Details ,ShareDetails
# Register your models here.

@admin.register(Details)
class DetailsAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','image','Education']

@admin.register(LinkData)
class LinkDataAdmin(admin.ModelAdmin):
    list_display = ['id','user','nameLink','link']

@admin.register(ShareDetails)
class RegisterId(admin.ModelAdmin):
    list_display = ['id','user','nameid']