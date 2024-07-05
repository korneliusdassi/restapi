from django.urls import path
from bukus import views

urlpatterns = [
    path('bukus/', views.bukus_list),
    path('bukus/<int:id>/', views.bukus_detail),
]

