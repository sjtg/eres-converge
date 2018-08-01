from django.contrib import admin
from django.contrib.auth import views as auth_views
from eresapp import views as eres_views
from accounts import views as accounts_views
from django.conf.urls import url
from eresapp import views
from django.conf import settings
from django.conf.urls.static import static
from . import views as core_views

urlpatterns = [
url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage, name='HomePage'),
    # url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^board/$', views.PostList, name='PostList'),
    url(r'^board/post/(?P<pk>\d+)/$', views.PostDetail, name='PostDetail'),
    url(r'^board/post/new/$', views.PostNew, name='PostNew'),
    url(r'^board/post/(?P<pk>\d+)/edit/$', views.PostEdit, name='PostEdit'),
    url(r'^uploads/$', views.NewDocs, name='uploads'),
    url(r'^uploads/$', views.ReviewerDocs, name='uploads'),
    # url(r'^uploads/$', views.UploadView.as_view(), name='uploads'),
    url(r'^dashboard/$', views.Dashboard, name='dashboard'),
    url(r'^reviewer/$', views.dashboard_reviewer, name='reviewer'),
    url(r'^fees/$', views.Fees, name='fees'),
    url(r'^about/$', views.Aboutus, name='about'),
    url(r'^signup/$', accounts_views.signup, name='signup' ),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^reset/$',
        auth_views.PasswordResetView.as_view(
            template_name='password_reset.html',
            email_template_name='password_reset_email.html',
            subject_template_name='password_reset_subject.txt'
        ),
        name='password_reset'),
    url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
    url(r'^reset/done/$',
        auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/complete/$',
        auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
    url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
