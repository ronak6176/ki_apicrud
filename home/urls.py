from django.contrib import admin
from django.urls import path,include
from home import views
from rest_framework import routers
# from home.views import PersonViewSet

# router  = routers.DefaultRouter()
# router.register(r'user', PersonViewSet)   

urlpatterns = [

   #  path('', include(router.urls)),
  
   path('', views.ApiOverview, name='home'), 
   path('create/user', views.add_items, name='add-items'),
   path('all/user', views.view_items, name='view_items'),
   path('update/<int:pk>/', views.update_items, name='update-items'),   
   path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
   # path('', include(router.urls)),
# ###################################################################################33
   path('', views.ApiOverview, name='home'), 
   path('create/appointment', views.add_items, name='add-items'),
   path('all/appointment', views.view_items, name='view_items'),
   path('update/<int:pk>/', views.update_items, name='update-items'),   
   path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
   #################################################################################
   path('', views.ApiOverview, name='home'), 
   path('create/event_benefits', views.add_items, name='add-items'),
   path('all/event_benefits', views.view_items, name='view_items'),
   path('update/<int:pk>/', views.update_items, name='update-items'),   
   path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
]

# urlpatterns = [
   
#     path('', views.index, name="home"),
# ]