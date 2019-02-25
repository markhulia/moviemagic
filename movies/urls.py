from django.urls import path

from movies import views

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /movie/5/
    path('<int:movie_id>/', views.detail, name='detail'),
]