from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyPinterest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #
    url(r'^articles/comments/', include('django.contrib.comments.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'MyPinterest.User.views.login',name="login"),
    url(r'^signup$', 'MyPinterest.User.views.signup', name='signup'),
    url(r'^userpage$', 'MyPinterest.User.views.userpage'),
    url(r'^createboard','MyPinterest.Pinboard.views.createBoard'),
)
