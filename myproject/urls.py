from django.urls import path, include
from django.contrib.auth.views import LogoutView, LoginView
from snap import views
from snap.views import admin_password_reset

from snap.views import admin_dashboard_view, admin_404, add_registration_view, list_registration_view, update_registration_view, delete_registration_view,delete_selected_registrations_view


urlpatterns = [
    path('', views.index, name='index'),
    path('adminclick/', views.adminclick_view, name='adminclick'),
    path('adminlogin/', LoginView.as_view(template_name='admin/login.html'), name='adminlogin'),
    path('afterlogin/', views.afterlogin_view, name='afterlogin'),
    path('logout/', LogoutView.as_view(next_page='/adminlogin/'), name='logout'),
    path('admin-dashboard/', admin_dashboard_view, name='admin-dashboard'),
    path('add-registration/', add_registration_view, name='add-registration'),
    path('list-registration/', list_registration_view, name='list-registration'),
    path('admin/password/reset/', admin_password_reset, name='admin_password_reset'),
    path('update-registration/<int:registration_id>/', update_registration_view, name='update-registration'),
    path('delete-registration/<int:pk>/', delete_registration_view, name='delete-registration'),
    path('delete-selected-registrations/', delete_selected_registrations_view, name='delete-selected-registrations'),
    # ... Other URL patterns ...
    path('admin/404/', admin_404),
    path('', include("snap.urls")),
]



