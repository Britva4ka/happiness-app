from django.contrib import admin
from .models import Team, Member
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Team)
admin.site.register(Member, UserAdmin)
