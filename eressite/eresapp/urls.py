from django.conf.urls import url
from . import views
from . import views as core_views



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^board/$', views.post_list, name='post_list'),
    url(r'^board/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^board/post/new/$', views.post_new, name='post_new'),
    url(r'^board/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^upload/$', views.UploadView.as_view(), name='upload'),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^reviewer/$', views.dashboard_reviewer, name='reviewer'),

]
