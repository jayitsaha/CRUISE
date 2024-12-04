from django.urls import path
from . import views




urlpatterns = [
    path('num-passengers/', views.num_passengers, name='num_passengers'),
    path('add-passenger/', views.add_passenger, name='add_passenger'),
    path('invoice/<int:invoice_id>/', views.invoice_view, name='invoice'),
    path('success/', views.success, name='success'),
]
