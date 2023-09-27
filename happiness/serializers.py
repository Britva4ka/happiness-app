from rest_framework import serializers
from .models import Team, Member, Happiness


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
# TODO fix serializers. (put method want username and password)

    class Meta:
        model = Member
        fields = ['username', 'email', 'is_staff', 'password']
        read_only_fields = ['username', 'password']


class HappinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Happiness
        fields = '__all__'
