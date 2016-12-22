from django.conf.urls import url
from .views import viewArticle, viewArticles, disdate

urlpatterns = [
	url(r'^article/(\d+)/$', viewArticle, name='article'),
	url(r'^articles/(?P<month>\d{2})/(?P<year>\d{4})$', viewArticles, name="articles"),
	url(r'^articles/date/$', disdate, name="disdate"),
]