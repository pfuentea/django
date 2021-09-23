from django.shortcuts import render,redirect

# Create your views here.

def index(request):
    return render(request,'forms.html')

def create_user(request):
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    context = {
    	"name_on_template" : name_from_form,
    	"email_on_template" : email_from_form
    }
    return redirect("/success")

def success(request):
    # esta es la ruta de éxito
    return render(request,"success.html")


def reset(request):
    if request.session ['counter'] >= 9:
        request.session ['counter'] = 0
        return redirect('/random_word')
