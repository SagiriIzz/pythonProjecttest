from django.urls import path
from . import views
urlpatterns = [
  path('', views.index),
  path('vse', views.vse),
  path('ras', views.update),
path('fun', views.test),

]