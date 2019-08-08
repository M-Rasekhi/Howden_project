from django.urls import path
from . import views

app_name = 'calc_app'

urlpatterns = [
    path('section_prop/', views.rectangle, name='rectangle'),
    path('fan_unbalance/', views.fan_unbalance, name="fan_unbalance"),
    path('earthquake_load/', views.earth_quake, name="earth_quake"),
]
