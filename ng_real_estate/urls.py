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
    url(r'^testpage/', 'real_estate_main.views.testpage', name='testpage'),
    # url(r'^contact/thankyou/', 'contacts.views.thankyou'),
    # url(r'^contactt/', 'contacts.views.contactview'),

    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

# Not certain it should be 'honeymooning...' or 'real_estate_main...'
    (r'^$', 'honeymooning.blog.views.index'),
    url(r'^homess/view/(?P<slug>[^\.]+).html', 'real_estate_main.homess.views.view_post', name='view_homess_post'),
    url(r'^homess/category/(?P<slug>[^\.]+).html', 'real_estate_main.homess.views.view_category', name='view_homess_category'),
)
