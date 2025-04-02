from django.urls import path
from posts import views

urlpatterns = [
    # path('', views.Home, name= 'home'),
    path('', views.HomeView.as_view(), name='home'),
    # path('<int:id>', views.post, name='post'),
    path('<int:pk>', views.PostView.as_view(), name= 'post'),
    path('tags/<int:id>', views.tag, name='tag'),
    # path('search',views.search, name='search')
    path('search',views.SearchView.as_view(), name='search')
]