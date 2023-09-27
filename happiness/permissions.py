from rest_framework import permissions
from .models import Happiness
import datetime


class UniqueHappinessPermission(permissions.BasePermission):
    message = "Happiness for today already exists"

    def has_permission(self, request, view):
        if request.method == 'POST':
            user = request.user
            existing_happiness = Happiness.objects.filter(member_id=user.id, date=datetime.date.today()).exists()
            if existing_happiness:
                return False

        return True


class OwnerOnlyPermission(permissions.BasePermission):
    message = "You don't have permission to change another member's data"

    def has_permission(self, request, view):
        data_id = request.data.get('member')
        if data_id and request.user.id == int(data_id) or request.user.is_staff or request.user.is_superuser:
            return True
        return False
