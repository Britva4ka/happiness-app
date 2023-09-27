from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets, permissions
from .models import Team, Member, Happiness
from .serializers import TeamSerializer, MemberSerializer, HappinessSerializer
from .permissions import UniqueHappinessPermission, OwnerOnlyPermission


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = []


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    permission_classes = []


class HappinessViewSet(viewsets.ModelViewSet):
    queryset = Happiness.objects.all()
    serializer_class = HappinessSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.IsAuthenticatedOrReadOnly()]
        else:
            return [permissions.IsAuthenticated(), OwnerOnlyPermission(), UniqueHappinessPermission()]
