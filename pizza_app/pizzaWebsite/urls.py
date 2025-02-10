from django.urls import path
from . import views

urlpatterns = [
   path('', views.gologin, name="gologin"),
   path('login/', views.login, name="login"),
   path('signup/', views.signup, name="signup"),
   path('home/', views.home, name="home"),
   path('pizza_selection/', views.selection, name="selection"),
   path('cart/', views.cart, name="cart"),
   path('payment/', views.payment, name="payment"),
]