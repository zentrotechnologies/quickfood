from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    # Template rendering URLs
    path('', views.landing_page, name='landing_page'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    # path('dashboard/', views.dashboard, name='dashboard'),

    # path('customer-registration/', views.customer_registration, name='customer_registration'),


]