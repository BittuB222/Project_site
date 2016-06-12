from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'testFunction',views.testFunction),
    url(r'insertdata',views.insertdata),
    url(r'insertdotas',views.insertdotas),
    url(r'page1/(?P<nid>[-\w]+)$',views.page1),
    url(r'page2',views.page2),
    url(r'page3',views.page3),
    url(r'page4',views.page4),
    url(r'page5',views.page5),
]