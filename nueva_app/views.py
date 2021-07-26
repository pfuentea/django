from django.shortcuts import render, HttpResponse,redirect
from django.http import JsonResponse

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
    var_json={'foo': 'bar'}
    return JsonResponse(var_json)