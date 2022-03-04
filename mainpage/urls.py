from django.conf.urls import url
from .views import ProjectListBadgesAndFormView
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', ProjectListBadgesAndFormView.as_view(), name='main'),
    url(r'^sitemap\.xml$', TemplateView.as_view(template_name='mainpage/sitemap.xml', content_type='text/xml')),
]
