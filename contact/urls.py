
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('save',views.save,name='save'),
    path('done',views.done,name='done'),
    path('home',views.all,name='all'),
    path('call',views.call,name='call')
]

urlpatterns += staticfiles_urlpatterns()
