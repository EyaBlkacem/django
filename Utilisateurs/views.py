from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
import re
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User






def Creation_compte(request):
  if request.method == "POST":
    username=request.POST['username']
    email=request.POST['email']
    password_confirm=request.POST['password_confirm']



    if password != password_confirm:
      messages.error(request, "les mots de passe ne sont pas identiques. veuillez réssayer") 
      return redirect ("creation")




    if len(password)<8 or not re.search (r'[A-Z-a-z]',password) or not re.search(r'\d', password) or not re.search(r'[!@#$%(),.?":{}`|]', password):
      messages.error(request, 'le mot de passe doit contenir au moins 8 caractéres , incluant des lettres , des chiffres , et des caractéres spéciaux')
      return redirect("creation")
    
    try:
      validate_email(email)
    except ValidationError:
       messages.error(request, "L'adresse e-mail invalide. veuillez réessayer. ")

       return redirect  ("creation")
    
    if User.objects.filter(username=username).exists():
     messages.error(request, "ce nom d'utilisateur existe déja.Veuillez ressayer ")
     return redirect("creation")
    if User.objects.filter(email=email).exists():
      messages.error(request, "cette adresse e-mail est déja utilisé, Veuillez réessayer ")
      return redirect("creation")
    



    User.objects.create_user(username=username, email=email,password=password)
    messages.success(request, "compte crée avec succés . Connectez-vous maintenant. ")
    return redirect ('login')
  return render(request, "creation.html")













# Create your views here.
def connecter_compte(request):
    if request.POST=="POST":
 
      username = request.POST.get('username')

      password= request.POST.get('password')
    

      user= authenticate(request, username= username, password= password)

      if user is not None :
        login(request, user )
        return redirect('acc')
    

      else:
       messages.error(request, "Nom d'utilisateur ou mot de passe incorrect. ")
      return redirect("login")
    
    return render (request,'login.html' )



def Verification_Mail(request) :
  if request.method =="POST":
    email = request.POST.get('email')


    if not email:
      messages.error(request, "veuillez rentrer une adresse mail valide.")
      return(request, "verificationMail.html ")
    user = User.objects.filter(email=email).first
    if user :
      
      return redirect("modifier", email=email )
    else:
      messages.error(request, "cette adresse ne correspond a aucun compte.Veuillez réessayer avec une autre ou créez un compte")
      return redirect("verification")
    
  return render(request, "verificationMail.html")




def Changement_code(request, email):
  
  try :
    user= User.objects.get(email=email)
  except User.DoesNotExist:
    messages.error(request, "L'utilisateur Introuvable") 
    return redirect ("login")
  if request.method== "POST":
    password= request.POST.get('password')
    password_confirm= request.POST.get('password_confirm')




    if password== password_confirm:
      if len(password)<8:
        messages.error(request, "le mot de passe doit contenir au moins 8 caractéres.")
    elif not  any(char.isdigit() for char in password):
      messages.error(request, "le mot de passe doit contenir au moins un chiffre ")
    elif not any(char.isalpha()for char in password)  :
      messages.error(request, "le mot de passe doit contenir au moins une lettre")

    else:
      user.set_password(password)
      user.save()
      messages.success(request,"le mot de passe a bien été modifié;connectez-vous maintenant")
      return redirect("login")
    
  else:
        messages.error(request, "les mots de passe ne correspondent pas.Réessayez")

  context={
       'email':email

}        
  return render(request, "nouveauMDP.html",context)

    
    




      






    


      
      


     
 
    
    

      
    


     

 
