from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('users', views.UsersView.as_view()),
    path('users/<int:pk>', views.UserView.as_view()),
    path('menu', views.MenuView.as_view()),
    path('menu/<int:pk>', views.MenuItemView.as_view()),
    path('booking/tables', views.BookingView.as_view()),
    path('booking/tables/<int:pk>', views.BookingView.as_view()),
]