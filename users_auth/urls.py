from django.urls import path
from users_auth.views import login_view, logout_view, dashboard_view

urlpatterns = [
    path('', login_view, name='login_view'),
    path('dashboard/', dashboard_view, name='dashboard_view'),
    path('logout/', logout_view, name='logout_view'),
]