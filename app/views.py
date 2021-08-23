from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from .forms import UserForm, PostForm
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login

#decorador de vistas obligatorias
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


from .models import Post

# Páginacion
from django.core.paginator import Paginator
from django.http import Http404



# redireccionar por nombre de url
from django.urls import reverse




# Create your views here.
def home(request):
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def login_view(request):
    if request.method=='POST':
        username = request.POST['usuarioLogin']
        password = request.POST['contraseñaLogin']
        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:    
            return render(request,'usuario/login.html',{'error':'Usuario o contraseña incorrecto'})
    
    return render(request,"usuario/login.html")

def registro(request):

    if request.method =='POST':
        username = request.POST['username']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        email = request.POST['email']
        contraseña = request.POST['contraseña']
        contraseña2 = request.POST['contraseña2']

        if contraseña != contraseña2:
            return render(request,'usuario/registro.html',{'error':'Las contraseñas deben coincidir'})
        
        try:
            userNew = User.objects.create_user(username=username,password=contraseña)
        except IntegrityError:
            return render(request, 'usuario/registro.html', {'error': 'este usuario ya se encuentra registrado'})
        userNew.first_name = nombre
        userNew.last_name = apellido
        userNew.email = email
        userNew.save()
        messages.success(request, '¡Usuario creado correctamente!')
        return redirect('home')



    return render(request,"usuario/registro.html")


def perfil(request):
    posts = Post.objects.all().filter(user_id=request.user.id)

    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(posts, 4)
        posts = paginator.page(page)
    except:
        raise Http404

    data = {
        'entity':posts,
        'paginator': paginator
    }
    return render(request,'usuario/perfil.html',data)

def crear_post(request):
    if request.method =='POST':
        titulo=request.POST.get('titulo')
        foto=request.FILES.get('foto')
        descripcion=request.POST.get('descripcion')
        user=request.user.id
        new_post=Post(titulo=titulo,foto_post=foto,descripcion=descripcion,user_id=user)
        new_post.save()
        messages.success(request, 'Publicación creada correctamente')
        return redirect('perfil')

    return render(request,'post/subir_post.html')


def post(request,id):
    post = Post.objects.get(id=id)
    
    return render(request,'post/post.html',{'post':post})

def editar_post(request,id):
    post = Post.objects.get(id=id)

    if request.POST:
        print('submit')
        titulo = request.POST.get('titulo',False)
        descripcion = request.POST.get('descripcion',False)

        post.titulo=titulo
        post.descripcion=descripcion
        post.save()
        messages.success(request, 'Publicacion modificada correctamente')
        return redirect('perfil')
    return render(request,"post/editar_post.html",{'post':post})

def eliminar_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    messages.success(request, 'Post eliminado correctamente')
    return redirect('perfil')


def editar_perfil(request):
    usuario = request.user
    data = {'usuario':usuario}
    if request.POST:
        first_name= request.POST.get('nombre',False)
        last_name= request.POST.get('apellido',False)
        username= request.POST.get('username',False)
        email=request.POST.get('email',False)
        if first_name and last_name:
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.email = email
            request.user.save()
            data['exito']='Cambios realizados correctamente'
            return render(request, 'usuario/editar_perfil.html', data)

    
    return render(request,"usuario/editar_perfil.html",data)


def cambiar_contraseña(request):
    data={}
    if request.POST:
        password = request.POST.get('contraseña','')
        re_password = request.POST.get('contraseña2',False)
        if password == re_password:
            request.user.set_password(password)
            request.user.save()
            logout(request)
            data['exito']='Contraseña cambiada correctamente'
            
        else:
            data['error']='Las contraseñas deben coincidir'
            return render(request,'usuario/editar_perfil.html',{'error':'Las contraseñas deben coincidir'})

    return HttpResponseRedirect(reverse('editar_perfil'))




def adm_usuarios(request):


    usuarios = User.objects.all()
    page = request.GET.get('page', 1)
    try:
        paginator = Paginator(usuarios, 8)
        usuarios = paginator.page(page)
    except :
        raise Http404

    data = {
        'entity':usuarios,
        'paginator': paginator
    }
    
    return render(request,'admin/adm_usuarios.html',data)

    

@staff_member_required(login_url = 'home')
@login_required(login_url = "login")
def eliminar_usuario(request,id):
    usuario = get_object_or_404(User, id=id)
    usuario.delete()
    messages.success(request, 'Usuario eliminado correctamente')
    return redirect('adm_usuarios')

@staff_member_required(login_url = 'home')
@login_required(login_url = "login")
def adm_posts(request,id):
    posts = Post.objects.all().filter(user_id=id)
    user = User.objects.get(id=id)
    data = {
        'posts':posts,
        'user': user
    }
    return render(request,'admin/adm_post.html',data)


@staff_member_required(login_url = 'index')
@login_required(login_url = "login")
def eliminar_post(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('adm_usuarios'))



def alimentacion(request):
    return render(request, 'ejercicios/alimentacion.html')

def espalda(request):
    return render(request, 'ejercicios/espalda.html')

def piernas(request):
    return render(request, 'ejercicios/piernas.html')

def triceps(request):
    return render(request, 'ejercicios/triceps.html')