from django.urls import path
from . import views
app_name = 'services'
urlpatterns = [
    path('', views.products, name='products-list'),
    path('<int:pk>/', views.product, name='product-detail'),
    path('send-message/', views.send_message, name='send-message'),
]