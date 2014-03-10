from django.conf.urls import patterns, include, url
from myapp.views import LandingPage, AddStudent, defaultLandingPage

urlpatterns = patterns('',
    url(r'^add/', AddStudent.as_view(), name="add_subscriver"),
    url(r'^1/$', defaultLandingPage, name="landing1"),
    url(r'^$', LandingPage.as_view(), name="landing"),
)


from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
