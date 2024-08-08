from django.urls import path
from frontend import views


urlpatterns = [
    path('', views.index, name='index'),
    path('pricing/', views.pricing, name='pricing'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('register-artisan/', views.register_artisan, name='register_artisan'),
    path('register-artisan-step-2/', views.save_activity_info, name='register_artisan_step_2'),
    path('register-artisan-step-3/', views.save_activity_location, name='register_artisan_step_3'),
    path('create-service/', views.create_service, name='create_service'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/messages', views.dashboard_messages, name='dashboard_messages'),
    path('dashboard/services', views.dashboard_services, name='dashboard_services'),
    path('dashboard/services/<int:service_id>/', views.dashboard_service_detail, name='dashboard_service'),
    path('dashboard/services/create/', views.create_service, name='dashboard_add_service'),
    path('dashboard/services/<int:service_id>/delete/', views.delete_service, name='delete_service'),
    path('dashboard/services/<int:service_id>/edit/', views.edit_service, name='edit_service'),
    path('dashboard/profile-edit/', views.edit_profile, name='edit_profile'),
    path('dashboard/user-profile/', views.update_profile, name='user_profile'),

]
