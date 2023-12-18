from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name="index_page"),
    path('signup/',signup,name="signup"),
    path('login/',login,name="login"),
    path('logout/',logout,name="logout"),

    # Dashboard urls
    path('dashboard/',dashboard,name="dashboard"),
    path('dashboard/vehicles/',vehicles,name="vehicles"),
    path('dashboard/maps/',maps,name="maps"),
    path('dashboard/deliveries/',deliveries,name="delivery"),
    path('dashboard/vehicles/add_delivery/',add_delivery,name="add_delivery"),
    path('dashboard/vehicle_table/',vehicle_table,name="vehicle_table")


]








