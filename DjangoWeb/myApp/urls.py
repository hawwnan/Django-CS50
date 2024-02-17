# define a variable urlpatterns which is a list of all the allowable 
# URLs that can be accessed for this app
#in order to create urls
from django.urls import path 
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("hannan/", views.hannan, name="hannan"),
    path("david/", views.david, name="david")
]