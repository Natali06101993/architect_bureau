from django.shortcuts import render
from .forms import MyClientForm


# Create your views here.
def index(request):
    return render(
        request,
        'mainpage/index.html'
    )
    
def form(request):
    print('kuku')
    print(MyClientForm())
    return render(
        request,
        'mainpage/form.html',
        {
            'my_client_form': MyClientForm()
        }
    )

def company_description(request):
    return render(
        request,
        'mainpage/company_description.html'
    )
      
      
def my_project1(request):
    return render(
        request,
        'mainpage/my_project1.html'
    )
      
def my_project2(request):
    return render(
        request,
        'mainpage/my_project2.html'
    )


        


    
    

   