from django.conf.urls import patterns, include, url

from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='base.html'), name='base'),
    # url(r'^groomer_v2/', include('groomer_v2.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    # URL for logout
    url(r'^accounts/logout/$', 'accounts.views.logout_view', name='auth_logout'),
    # URL for login
    url(r'^accounts/login/$', 'accounts.views.login_view', name='auth_login'),
    # URL for registracii
    url(r'^accounts/registration/$', 'accounts.views.registration_view', name='auth_regitration'),

)
