from django.urls import path

from movies import views

app_name='movies'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # ex: /movies/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]