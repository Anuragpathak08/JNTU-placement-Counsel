from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),
    path('start-test/<uuid:test_uuid>/', views.start_test, name='start_test'),
]