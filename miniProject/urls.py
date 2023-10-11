from django.urls import path

from miniProject import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('project', views.project, name = 'project'),
    path('analysis', views.analysis, name = 'analysis'),
]