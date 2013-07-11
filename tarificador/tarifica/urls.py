from django.conf.urls import patterns, url
from tarifica import views

urlpatterns = patterns('',
                       url(r'setuptroncales$', views.setupUno, name = 'setup'),
                       url(r'thanks$', views.thanks, name = 'gracias'),
                       url(r'contact$',views.thanks, name = 'contacto'),
)