from rest_framework import routers
from happiness.views import TeamViewSet, MemberViewSet, HappinessViewSet

api_router = routers.DefaultRouter()
api_router.register(r'teams', TeamViewSet)
api_router.register(r'members', MemberViewSet)
api_router.register(r'happiness', HappinessViewSet)
