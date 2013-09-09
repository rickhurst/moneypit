from django.conf.urls import patterns, url

urlpatterns = patterns('tcoapp.views',

	url(r'^journeys/$', 'journeys'),

    url(r'^drf/journeys/$', 'journey_list'),
    url(r'^drf/journeys/(?P<pk>[0-9]+)/$', 'journey_detail'),
)