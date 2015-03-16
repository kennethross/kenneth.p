from django.conf.urls import patterns, include, url
from django.contrib import admin

from upload import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dengue.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^upload/$', 'upload.views.uploadBatchData', name ='name'),
    url(r'^abcdisplay/$','upload.views.abcdisplay'),
    url(r'^viewdata/$','upload.views.dataViewDisplay'),
    url(r'^admin/', include(admin.site.urls)),

    #user auth urls
    url(r'^accounts/login/$', 'auth_user.views.login'),
    url(r'^accounts/auth/$', 'auth_user.views.auth_view'),
    url(r'^accounts/logout/$', 'auth_user.views.logout'),
    url(r'^accounts/loggedin/$', 'auth_user.views.loggedin'),
    url(r'^accounts/invalid/$', 'auth_user.views.invalid_login'),
)
