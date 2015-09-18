from django.conf.urls import include, url, patterns
from django.contrib import admin
from auction_men import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^bidplacing/', include('bidplacing.urls', namespace='bidplacing')),

    url(r'^$', 'bidplacing.views.main_page', name='main_page'),

    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^accounts/profile/', 'bidplacing.views.profile_page', name='profile_page'),

]
if settings.DEBUG:
    urlpatterns += patterns('', (r'^bidplacing/media/(?P<path>.*)$', 'django.views.static.serve',
                                 {'document_root': settings.MEDIA_ROOT}))