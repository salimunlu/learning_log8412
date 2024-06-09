from django.urls import path

from . import views

app_name = 'learning_logs'

# Ana sayfa URL'i views modülündeki index görünümüne (fonksiyonuna) yönlendirilir.
urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
]
