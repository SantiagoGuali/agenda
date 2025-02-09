from unittest import result
from django.shortcuts import get_object_or_404, redirect, render, get_list_or_404
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string

@login_required
def home(request):
    return render(request, "home.html")


#----------------------------------------------------------------------------------------
#USER
#----------------------------------------------------------------------------------------


@login_required
def user_list_view(request):
    data = Usuario.objects.all()
    return render(request, "user/user_list.html", {'users':data})


def user_add_view(request):
    return render(request, "user/user_add.html")


@login_required
def user_form(request, id=None):
    if request.method == "POST":
        try:
            name = request.POST["name"]
            mail = request.POST["mail"]
            password = request.POST["pass"]
            code = request.POST["code"]
            profile = request.POST["profile"]
            state = int(request.POST.get("state", 0))
            stateManager = int(request.POST.get("stateManager", 0))
#update
            if id:  
                usuario = get_object_or_404(Usuario, codigo_usu=id)
                usuario.nombre_usu = name
                usuario.email_usu = mail
                usuario.password_usu = password
                usuario.codigo_uni = code
                usuario.perfil_usu = profile
                usuario.estado_usu = state
                usuario.es_delegado = stateManager
                usuario.save()
                messages.success(request, "Usuario actualizado correctamente")
#insert
            else:
                Usuario.objects.create(
                    nombre_usu=name,
                    email_usu=mail,
                    password_usu=password,
                    codigo_uni=code,
                    perfil_usu=profile,
                    estado_usu=state,
                    es_delegado=stateManager
                )
                messages.success(request, "Usuario registrado correctamente")

            return redirect("user_list")

        except Exception as e:
            messages.error(request, f"Error al procesar el usuario: {str(e)}")

    else:  
        usuario = None
        if id:
            usuario = get_object_or_404(Usuario, codigo_usu=id)

        return render(request, "user/user_add.html", {"usuario": usuario})

    

def user_del(request, id):
    try:
        data = Usuario.objects.get(codigo_usu = id)
        data.delete()
        messages.success(request, "Eliminado correctamente")
        return redirect('user_list')
    except Exception as e:
        messages.success(request, f"error: {str(e)}")


#----------------------------------------------------------------------------------------
#PROJECT
#----------------------------------------------------------------------------------------
@login_required
def project_list_view(request):
    data = Proyecto.objects.all()
    return render(request, "project/project_list.html", {'projects':data})



#----------------------------------------------------------------------------------------
#VOCATIVE
#----------------------------------------------------------------------------------------
@login_required
def vocative_list_view(request):
    data = Vocativo.objects.all()
    return render(request, "vocative/vocative_list.html", {'vocatives':data})



#----------------------------------------------------------------------------------------
#DELEGATE
#----------------------------------------------------------------------------------------
@login_required
def delegate_list_view(request):
    data = Delegado.objects.all()
    return render(request, "delegate/delegate_list.html", {'delegates':data})



#----------------------------------------------------------------------------------------
#NOTIFICATION
#------------------------------------------------------ ----------------------------------
@login_required
def notification_list_view(request):
    data = Notificacion.objects.all()
    return render(request, "notification/notification_list.html", {'notifications':data})



#----------------------------------------------------------------------------------------
#ADDRESS
#----------------------------------------------------------------------------------------
@login_required
def address_list_view(request):
    data = Direccion.objects.all()
    return render(request, "address/address_list.html", {'address':data})


#----------------------------------------------------------------------------------------
#INVESTEMENT
#----------------------------------------------------------------------------------------
@login_required
def investment_list_view(request):
    data = AyudaMemoria.objects.all()
    return render(request, "investment/investment_list.html", {'investments':data})


#----------------------------------------------------------------------------------------
#EVENT
#----------------------------------------------------------------------------------------
@login_required
def event_list_view(request):
    data = Evento.objects.all()
    return render(request, "event/event_list.html", {'events':data})








