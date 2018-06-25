import django_filters
from django.db.models import Q
from django.utils.translation import ugettext_lazy as _

from feed.models import FeedItem


class FeedItemFilter(django_filters.FilterSet):
    ALL_POST = 'all'
    MY_POST = 'my'
    TRACKING_POST = 'tracking'

    POST_CHOICES = (
        (MY_POST, _('My posts')),
        (TRACKING_POST, _('Me and the posts of everyone I\'m tracking')),
        (ALL_POST, _('Everybody\'s posts')),
    )

    post = django_filters.ChoiceFilter(choices=POST_CHOICES, method='filter_post')

    class Meta:
        model = FeedItem
        fields = ('post',)

    def filter_post(self, queryset, name, value):
        if value == self.MY_POST:
            return queryset.filter(user=self.request.user)

        elif value == self.TRACKING_POST:
            user = self.request.user
            users = user.registered_user.tracking.all().values_list('user_id', flat=True)
            return queryset.filter(Q(user=user) | Q(user__in=users))

        return queryset
