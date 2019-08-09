from rest_framework import serializers
from ..models.recentlyviewd import RecentlyViewd


class RecentlyViewdSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecentlyViewd
        fields = '__all__'
