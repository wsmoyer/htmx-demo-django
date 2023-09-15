from django.contrib import admin
from django.contrib.auth import logout
from django.urls import path
from django.conf.urls import include
from apps.users import views
from apps.players import views as player_views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('logout/', logout, {'next_page': '/'}, name='logout'),
    path('api/', include('htmxdemo.api_urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("", views.home, name="home"),
    path("auth", views.auth, name="auth"),
    path('create-player', player_views.PlayerFormView.as_view(), name="create-player")    


    #  path("", views.home, name="home"),

]
