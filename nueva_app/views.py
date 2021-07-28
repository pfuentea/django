from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse
from time import gmtime, strftime,localtime

# Create your views here.
def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def root(request):
    return redirect("/")

def create(request):
    return redirect("/")

def show(request,my_val):
    return HttpResponse(f"placeholder para mostrar el blog numero: {my_val}")
    
def edit(request,my_val):
    return HttpResponse(f"placeholder para editar el blog {my_val}")

def destroy(request,my_val):
    return redirect("/blogs")
    
def json(request):
    var_json={
        'nombre': 'Washimingo',
        'apellido': 'de Washimingo',
        'edad': '25',
    }
    return JsonResponse(var_json)

def home(request):
    return render(request,'home.html')


def home2(request,p_name):
    context={
        "nombre_principal":p_name, 
        "nombres":["Pato1","Pato2","Pato3"]
    }
    return render(request,'home.html',context)

def grogu(request):
    context={
        "imgs":["https://sm.ign.com/ign_es/screenshot/default/mandalorian-baby-yoda-macarons_1nqk.jpg",
        "https://i.blogs.es/744f32/yoda/450_1000.jpg",
        "https://e00-marca.uecdn.es/assets/multimedia/imagenes/2020/01/15/15791135281802.jpg",
        "https://www.tonica.la/__export/1585686309389/sites/debate/img/2020/03/31/baby_yoda_2_1.jpg_1037907269.jpg"]
    }
    return render(request,'grogu.html',context)

def mandalorian(request):
    context={
        "imgs":["https://media.revistagq.com/photos/5fe1bab3610ba5db8e942284/1:1/w_1600%2Cc_limit/mandalorian_ver25_xlg.jpg",
        "https://mediaproxy.salon.com/width/1200/https://media.salon.com/2020/12/the-mandalorian-still09.jpg",
        "https://www.gamerfocus.co/wp-content/uploads/2019/12/the-mandalorian-0.jpeg",
        "https://i.etsystatic.com/23511185/r/il/39216b/2385625302/il_570xN.2385625302_7lg9.jpg"]
    }
    return render(request,'mando.html',context)

def  time_display(request):
    context={
        "day":strftime("%d", localtime()),
        "mes":strftime("%b", localtime()),
        "date": strftime("%d %B %Y", localtime()),
        "time": strftime("%H:%M:%S %p", localtime())
    }
    return render(request,'time_display.html',context)