from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions

from feed.filters import FeedItemFilter
from feed.models import FeedItem
from feed.serializers import FeedItemSerializer


class FeedListView(generics.ListAPIView):
    """
    Filter user's posts
    ---
    list:
        parameters:

            - name: post
              type: string
              enum: [all, my, tracking]
              description: by posts
              paramType: query
    """
    permission_classes = (permissions.IsAuthenticated,)
    queryset = FeedItem.objects.all()
    serializer_class = FeedItemSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = FeedItemFilter
