from django.urls import path
from . import views
urlpatterns = [
    path('', views.index_colormania, name='index_colormania'),
    
    path('login-usuario/', views.login_usuario, name='login_usuario'),
    path('logout/', views.logout_usuario, name='logout_usuario'),
    path('registro/', views.registro, name='registro'), 
    
    path('admin-login/', views.login_admin, name='login_admin'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('index-admin/', views.index_admin, name='index_admin'),
    path('admin-pinturas/', views.admin_pinturas, name='admin_pinturas'),
    path('admin-productos/', views.admin_productos, name='admin_productos'),
    path('admin-selladores/', views.admin_selladores, name='admin_selladores'),
    path('admin-colores/', views.admin_colores, name='admin_colores'),
    path('admin-logout/', views.logout_admin, name='logout_admin'),
    
    path('pinturas/', views.ver_pinturas, name='ver_pinturas'),
    path('selladores/', views.ver_selladores, name='ver_selladores'),
    path('productos/', views.ver_productos, name='ver_productos'),
    
    
]