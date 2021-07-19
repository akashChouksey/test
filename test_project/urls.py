from django.contrib import admin
from django.urls import path
from test_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_user, name='all_user'),
    path('add/user', views.add_user, name='add_user'),
    path('delete/user', views.delete_user, name='delete_user'),
]
