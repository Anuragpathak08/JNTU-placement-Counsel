from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_home, name='dash-board'),
    path('test/<int:test_id>/', views.test_results, name='test_results'),
]