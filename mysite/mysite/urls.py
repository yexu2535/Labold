# coding = 'utf-8'

from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from books import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),
#    url(r'^$', 'print.views.index', name='home'),
    
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^home/$', views.display),
    (r'^delete/$', views.delete),
#    (r'^search-form/$', views.search_form),
    (r'^search/$', views.search),
    (r'^details/$', views.details),
    (r'^add_book/$', views.add_book),
    (r'^add_author/$', views.add_author),
    (r'^add/success/$', views.success),
    (r'^update/$', views.update),
    (r'^update/success/$', views.update_success),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
