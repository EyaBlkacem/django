from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.
def connecter_compte(request):
    if request.POST=="POST":
 
      username = request.POST.gt('username')
      password= request.POST.get('password')
    

      user= authenticate(request, username= username, password= password)

      if user is not None :
        login(request, user )
        return redirect('acc')
    

      else:
       messages.error(request, "Nom d'utilisateur ou mot de passe incorrect. ")
      return redirect("login")
    
    return render (request,'login.html' )
 
    
    

      
    


     

 
