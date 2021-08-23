from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # USERS
    path('perfil/', views.perfil, name='perfil'),
    path('editar-perfil/',views.editar_perfil, name='editar_perfil'),
    path('cambiar-clave/',views.cambiar_contraseña,name='cambiar_clave'),

    # POSTS
    path('crear-post/', views.crear_post, name='crear_post'),
    path('post/<int:id>/',views.post,name='post'),
    path('editar-post/<int:id>/', views.editar_post, name='editar_post'),
    path('eliminar-post/<int:id>/', views.eliminar_post, name='eliminar_post'),

    # ADMIN
    path('administrar-usuarios',views.adm_usuarios, name='adm_usuarios'),
    path('eliminar-usuario/<int:id>/',views.eliminar_usuario,name="eliminar_usuario"),
    path('adm-publicaciones/<int:id>',views.adm_posts, name='adm_posts'),
    path('eliminar-post/<int:id>',views.eliminar_post,name='eliminar_post'),

    #Ejercicios
    path('alimentacion',views.alimentacion,name='alimentacion'),
    path('espalda',views.espalda,name='espalda'),
    path('triceps',views.triceps,name='triceps'),
    path('piernas',views.piernas,name='piernas'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
