from django.shortcuts import redirect, render
from .models import Country, Trafood, Language, bestPlace
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .filters import CountryFilter
# Create your views here.


def registerPage(request):
    form = CreateUserForm()

    if request.method =='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()      
            user = form.cleaned_data.get('username')
            messages.success(request,'Accout has been created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request,'log/register.html',context)

def loginPage(request):

    if request.method == 'POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main')
        else : 
            messages.info(request, 'Username of password is incorrect')

    context = {} 
    return render(request,'log/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('main')


def main(request):

    # All the work should be here
    country = Country.objects.all()
    myFilter = CountryFilter(request.GET , queryset = country)
    country = myFilter.qs
    title = 'Virtual Travel'
    context = {
        'title' : title,
        'countries' : country,
        'myFilter' :myFilter,
    }
    return render(request,'home.html',context)

@login_required(login_url='login')
def content(request,pk):

    # All the work should be here

    country = Country.objects.get(id=pk)
    language = country.language_set.all()
    bestplace = country.bestplace_set.all()
    trafood = country.trafood_set.all()

    title = 'Country name' # The country name should be here
    context = {
        'title' : title,
        'countries' : country,
        'languages' : language,
        'bestplace' : bestplace,
        'trafood' : trafood,
    }
    return render(request,'country.html',context)