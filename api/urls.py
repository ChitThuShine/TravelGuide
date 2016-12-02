from django.conf.urls import url
from api.views import category,users,lieux
from rest_framework_cache.registry import cache_registry

cache_registry.autodiscover()

urlpatterns = [
        url(r'^category/$',
            category.CategoryListView.as_view(),
            name='category_list'),
        url(r'^category/(?P<pk>\d+)/$',
            category.CategoryDetailView.as_view(),
            name='category_detail'),

        url(r'^appuser/$',
            users.AppUserListView.as_view(),
            name='appuser_list'),
        url(r'^appuser/(?P<pk>\d+)/$',
            users.AppUserDetailView.as_view(),
            name='appuser_detail'),

        url(r'^lieux/$',
            lieux.LieuListView.as_view(),
            name='lieux_list'),
        url(r'^lieux/(?P<pk>\d+)/$',
            lieux.LieuDetailView.as_view(),
            name='lieu_detail'),
]
