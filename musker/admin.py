from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile,Meep

# Register your models here.
admin.site.unregister(Group)


# Mix Profile info  User info
class ProfileInline(admin.StackedInline):
    model = Profile


# Extend  User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # just  display username fileds on admin page
    fields = ['username']
    inlines = [ProfileInline]


# unregister  initial User
admin.site.unregister(User)

# Register User and Profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)


# Register Meep
admin.site.register(Meep)