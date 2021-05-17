from django.contrib import admin
from django.urls import path
from first_app import views

admin.site.site_header = "SUMSUNG GALAXY"
admin.site.site_title = "SUMSUNG GALAXY Portal"
admin.site.index_title = "Welcome to SUMSUNG GALAXY"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('beach/', views.beach, name='beach'),
    path('blue/', views.blue, name='blue'),
    path('other/', views.other, name='other'),
]

