from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^boardpage','MyPinterest.Pinboard.views.boardpage'),
    url(r'^newpin','MyPinterest.Pinboard.views.newpin'),
    url(r'^pin','MyPinterest.Pinboard.views.pinpage'),
    url(r'^repin',"MyPinterest.Pinboard.views.repin"),
    #static serve
    url(r'^imgs(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
)
