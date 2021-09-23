from django.shortcuts import render,redirect
from random import randint, uniform,random

# Create your views here.
class resultado():
    def __init__(self,p_mensaje,p_estilo):
        mensaje=p_mensaje
        style=p_estilo

def index(request):
    request.session['mensajes']=[]
    request.session['gold']=0
    return render(request,'ninja.html')

def process_money(request,ubi):
    
    if request.method == "POST":
        #accion=request.POST['accion']
        accion=ubi
        mensaje=""
        if accion == 'farm':
            ganancia=randint(10,20)
        elif accion == 'cave':
            ganancia=randint(5,10)
        elif accion == 'house':
            ganancia=randint(2,5)
        elif accion == 'casino':
            ganancia=randint(-50,50)
        elif accion == 'reset':
            request.session['gold']=0
            ganancia=0
            request.session['mensajes']=[]
        
        request.session['gold']+=ganancia

        mensaje=str(ganancia)+" desde "+accion+"! ()"

        mensaje = f"{'Ganaste' if ganancia >= 0 else 'Perdiste'} {mensaje}"

        jeison={'mensaje':mensaje, 'style':'success' if ganancia >= 0 else 'danger'}
        request.session['mensajes'].append(jeison)
        request.session.save()

    context={
        }

    print(request.session['mensajes'] )
    return render(request,'ninja.html',context)
