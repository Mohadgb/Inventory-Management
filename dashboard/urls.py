from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.index, name='dashboard-index'),
    path('customers/', views.customers, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-product'),
    path('reservations/', views.reservations, name='dashboard-order'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
    path('customer/detail/<int:pk>/', views.customer_detail, name='dashboard-staff-detail'),
    path('order/saveDate', views.save_info, name='dashboard-order-saveDate'),


]