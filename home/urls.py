from django.contrib import admin
from django.urls import path,include
from home import views
from rest_framework import routers
# from home.views import PersonViewSet

# router  = routers.DefaultRouter()
# router.register(r'user', PersonViewSet)   

urlpatterns = [

   #  path('', include(router.urls)),
#######################################__user__############################################
   path('', views.ApiOverview, name='home'), 
   path('create/user', views.add_items, name='add-items'),
   path('all/user', views.view_items, name='view_items'),
   path('update/<int:pk>/', views.update_items, name='update-items'),   
   path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
   # path('', include(router.urls)),
#########################################__appointment__##########################################33
   path('', views.ApiOverview, name='home'), 
   path('create/appointment', views.appointment_add_items, name='appointment_add_items'),
   path('all/appointment', views.appointment_view_items, name='appointment_view_items'),
   path('update/<int:pk>/', views.update_items, name='update-items'),   
   path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
###############################################__history__##################################
   path('', views.ApiOverview, name='home'), 
   path('create/history', views.history_add_items, name='history_add_items'),
   path('all/history', views.history_view_items, name='history_view_items'),
   path('update/<int:pk>/', views.update_items, name='update-items'),   
   path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
   #######################################__event_benefits__############################################
   path('', views.ApiOverview, name='home'), 
   path('create/event_benefits', views.event_benefits_add_items, name='event_benefits_add_items'),
   path('all/event_benefits', views.event_benefits_view_items, name='event_benefits_view_items'),
   path('update/<int:pk>/', views.update_items, name='update-items'),   
   path('item/<int:pk>/delete/', views.delete_items, name='delete-items'),
   # path('', include(router.urls)),
]

# urlpatterns = [
   
#     path('', views.index, name="home"),
# ]