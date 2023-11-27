from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('api/vendors/', views.VendorDetails.as_view()),
    path('api/vendors/<int:pk>/', views.vendordetails, name='vendordetails'),
    path('api/purchase_orders/', views.PurchaseOrderDeatils.as_view()),
    
]
