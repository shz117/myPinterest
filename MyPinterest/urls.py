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
    url(r'^signout', 'MyPinterest.User.views.signout'),
    url(r'^user', 'MyPinterest.User.views.userprofile'),
    url(r'^changeemail',"MyPinterest.User.views.changeemail"),
    url(r'^userpage$', 'MyPinterest.User.views.userpage'),
    url(r'^createboard','MyPinterest.Pinboard.views.createBoard'),
    url(r'^createstream','MyPinterest.Pinboard.views.createStream'),
    url(r'^deletestream','MyPinterest.Relations.views.deletestream'),
    url(r'^boardpage','MyPinterest.Pinboard.views.boardpage'),
    url(r'^deleteboard','MyPinterest.Pinboard.views.deleteboard'),
    url(r'^newpin','MyPinterest.Pinboard.views.newpin'),
    url(r'^pin','MyPinterest.Pinboard.views.pinpage'),
    url(r'^deletepin','MyPinterest.Pinboard.views.deletepin'),
    url(r'^repin',"MyPinterest.Pinboard.views.repin"),
    url(r'^like',"MyPinterest.Relations.views.like"),
    url(r'^unlike',"MyPinterest.Relations.views.unlike"),
    url(r'^search',"MyPinterest.Pinboard.views.search"),
    url(r'^streampage',"MyPinterest.Relations.views.streampage"),
    url(r'^followboard',"MyPinterest.Relations.views.followboard"),
    url(r'^unfollowboard',"MyPinterest.Relations.views.unfollowboard"),
    url(r'^sendfriendrequest',"MyPinterest.Relations.views.friendrequesthandler"),
    url(r'^friendrequests',"MyPinterest.Relations.views.viewfriendrequests"),
    url(r'^acceptrequest',"MyPinterest.Relations.views.acceptrequest"),
    url(r'^rejectrequest',"MyPinterest.Relations.views.rejectrequest"),
    url(r'^recommend',"MyPinterest.Pinboard.views.recommend"),
    #static serve
    url(r'^imgs(?P<path>.*)$','django.views.static.serve',{'document_root': settings.MEDIA_ROOT }),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, }),
)
