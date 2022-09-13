from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import UserForm

# Create your views here.
def home(request):
    return render(request, 'base.html')

def about(request):
    return render(request, 'about.html')

def register(request):
    submitted = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/register?submitted=True')
    else:
        form =UserForm
        if 'submitted' in request.GET:
            submitted = True
    
    
    return render(request, 'register.html', {'form':form, 'submitted': submitted})