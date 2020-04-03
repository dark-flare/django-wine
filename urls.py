from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<int:wine_id>/', views.detail, name='detail'),
    path('drank/<int:wine_id>/', views.drank, name='drank'),
    path('recent', views.recent, name='recent')
]