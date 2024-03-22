from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('employee/<int:pk>/', views.employee_view, name='employee_detail'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('add_employee/', views.add_employee, name="add_employee"),
    path('update/<int:pk>/', views.update_employee, name='update'),
]