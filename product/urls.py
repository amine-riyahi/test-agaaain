from . import views
from django.urls import path


urlpatterns = [

     path('create',views.Create,name='create'),
     path('<int:productid>',views.Pdetails,name='Pdetails'),
     path('<int:productid>/upvote',views.upvote,name='upvote'),


]