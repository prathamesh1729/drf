from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	#url(r'^snippets/$', views.snippet_list),
	#url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),	
	#url(r'^msnippets/$', views.MSnippetList.as_view()),
	#url(r'^msnippets/(?P<pk>[0-9]+)/$', views.MSnippetDetail.as_view()),
	#url(r'^csnippets/$', views.CSnippetList.as_view()),
	#url(r'^csnippets/(?P<pk>[0-9]+)/$', views.CSnippetDetail.as_view()),
	url(r'^$', views.api_root),
	url(r'^snippets/$', views.SnippetList.as_view(), name = 'snippet-list'),
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(), name = 'snippet-detail'),
	url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(), name = 'snippet-highlight'),
	url(r'^users/$', views.UserList.as_view(), name = 'user-list'),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name = 'user-detail'),	
]

urlpatterns = format_suffix_patterns(urlpatterns)