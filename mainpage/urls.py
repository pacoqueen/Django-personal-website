from django.conf.urls import url
from .views import ProjectListBadgesAndFormView

urlpatterns = [
    url(r'^$', ProjectListBadgesAndFormView.as_view(), name='main')
]
