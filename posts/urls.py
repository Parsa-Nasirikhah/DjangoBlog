from django.urls import path
from posts import views

urlpatterns = [
    path('', views.Home, name= 'home'),
    path('<int:id>', views.post, name='post'),
    path('tags/<int:id>', views.tag, name='tag'),
    path('search',views.search, name='search')
]