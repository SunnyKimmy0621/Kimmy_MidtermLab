from django.urls import path
from TheLab.views import HomePageView, LoginPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='dashboard'),
    path('login/', LoginPageView.as_view(), name='login'),
]

