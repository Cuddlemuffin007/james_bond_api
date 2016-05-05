"""james_bond_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from api_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'api/movies/$', views.MovieListAPIView.as_view(), name='movie_list_api_view'),
    url(
        r'api/(?P<char_type>characters|allies|villains|henchmen|bond-girls)/$',
        views.CharacterListAPIView.as_view(),
        name='character_list_api_view'),
    url(r'api/vehicles/$', views.VehicleListAPIView.as_view(), name='vehicle_list_api_view'),
    url(r'api/gadgets/$', views.GadgetListAPIView.as_view(), name='gadget_list_api_view'),
    url(r'api/bond-actors/$', views.BondActorListAPIView.as_view(), name='bond_actor_list_api_view'),

    # Retrieve API Views for resources
    url(r'api/movies/(?P<pk>\d+)/$', views.MovieRetrieveAPIView.as_view(), name='movie_retrieve_api_view'),
    url(r'api/vehicles/(?P<pk>\d+)/$', views.VehicleRetrieveAPIView.as_view(), name='vehicle_retrieve_api_view'),
    url(r'api/gadgets/(?P<pk>\d+)/$', views.GadgetRetrieveAPIView.as_view(), name='gadget_retrieve_api_view'),
    url(
        r'api/bond-actors/(?P<pk>\d+)/$',
        views.BondActorRetrieveAPIView.as_view(),
        name='bond_actor_retrieve_api_view'),
    url(
        r'api/(?P<char_type>characters|allies|villains|henchmen|bond-girls)/(?P<pk>\d+)/$',
        views.CharacterByTypeRetrieveAPIView.as_view(),
        name='character_by_type_retrieve_api_view'
    )
]
