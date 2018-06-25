from rest_framework import serializers

from feed.models import FeedItem


class FeedItemSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = FeedItem
        fields = ('pk', 'content', 'username')
