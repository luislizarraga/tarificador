from django.conf.urls import patterns, url
from tarifica import views

urlpatterns = patterns('',
                       url(r'setuptroncales', views.setupUno, name = 'setup'),
)