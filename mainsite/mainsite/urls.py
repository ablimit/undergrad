from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'views.home', name='home'),
    url(r'^mainsite$', 'interview.views.sessiontest', name='sessiontest'),
    url(r'^interview$', 'interview.views.startInterview', name='interview'),
    url(r'^start$', 'interview.views.getInterviewQuestion', name='interviewquestions'),
    url(r'^nextround$', 'interview.views.getInterviewQuestion', name='interviewquestions'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
