from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('', views.index, name='home'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('accounts/login', views.signin, name='login'),
    path('profile', views.profile, name='profile'),
    path('business_list/', views.business, name='business'),
    path('post/', views.post_news, name='post'),
    path('new_hood/<username>', views.neighbourhood, name='hood'),
    path('welcome', views.welcome, name='welcome'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)