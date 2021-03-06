from __future__ import unicode_literals

from django.conf.urls import url
from django.utils.translation import ugettext_lazy as _

from . import views

urlpatterns = [
    url(_(r'^(?P<ranking_slug>[\w-]+)/?$'), views.RankingRedirect.as_view(), name="redirect"),
    url(_(r'^(?P<ranking_slug>[\w-]+)/information$'), views.RankingDetail.as_view(), name="detail"),
    url(_(r'^$'), views.RankingList.as_view(), name="list"),
]
