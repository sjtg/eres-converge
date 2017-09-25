from django.conf.urls import url
from . import views
from . import views as core_views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^student/$', views.student, name='student'),
    url(r'^reviewer/$', views.reviewer, name='reviewer'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^upload/$', views.UploadView.as_view(), name='upload'),
    url(r'^dashboard/$', core_views.message, name='dashboard'),

]
