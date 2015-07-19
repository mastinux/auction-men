from django.conf.urls import include, url, patterns
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'auction_men.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bidplacing/', include('bidplacing.urls', namespace='bidplacing')),
    url('^$', 'auction_men.views.main_page', name='main_page'),
    # url(r'auth/', include('auth_system.urls', namespace='auth')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/profile/', include('bidplacing.urls', namespace='bidplacing')),
]
