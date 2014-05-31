from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'real_estate_main.views.home', name='home'),
    url(r'^about/', 'real_estate_main.views.about', name='about'),
    url(r'^properties/', 'real_estate_main.views.properties', name='properties'),
    url(r'^contact/', 'real_estate_main.views.contact', name='contact'),
    url(r'^financing/', 'real_estate_main.views.financing', name='financing'),
    # url(r'^contact/thankyou/', 'contacts.views.thankyou'),
    # url(r'^contactt/', 'contacts.views.contactview'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
