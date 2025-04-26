from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView,CreateView,UpdateView,DetailView
from .models import Produits, Categories  # <-- bien écrire "Categories"
from .forms import AjoutProduit
from django.urls import reverse_lazy
from django.core.files.storage import FileSystemStorage
from .models import *
from django.http import JsonResponse


# Create your views here.
#def home(request):

 #   donnees= Produits.objects.all()

  #  context = {
   #     'donnees' : donnees
    #}
    #return render(request,'home.html', context)

class Affichage(ListView):

  
    template_name='home.html'

    queryset= Produits.objects.all()




class AjoutProduits(CreateView):


    model = Produits

    form_class = AjoutProduit
    template_name='ajout_donnees.html'
    success_url = reverse_lazy('home')

class update_donnees(UpdateView):
     
     model= Produits 

     form_class=AjoutProduit

     template_name='modification.html'
     success_url = reverse_lazy('home')

def supprimer(request, id):
     if request.method=="POST":
        produit=get_object_or_404(Produits, id=id)
        produit.delete()
        return JasonResponse({'success': True, 'message': "le produit a été supprimé avec succés"})
     return JasonResponse({'success': False, 'message': "Methode non autorisé"}) 

     

def recherche(request):
     query= request.GET.get('produit')
     donnees=Produits.objects.filter(name__icontains=query)
     context={
          'donnees' : donnees
     }
     return render(request,'resultat_recherche.html', context)


def Acc (request):
     return render(request, 'acc.html')


def detail(request, id):
     n=Produits.objects.get(id=id)

     return render(request, 'detail.html' {'n':n})     

     
class edit(DetailView):
     model = Produits
     template_name= 'detail.html'
     context_object_name='n'









def modifier(request, id):
       produit= get_object_or_404(Produits, id=id)
       categories= Categories.objects.all()
       errors={}

       if request.method=='POST' :
            name=request.POST.get('name')
            category_id=request.POST.get('category')
            price= request.POST.get('price')
            quantite= request.POST.get('quantite')
            description= request.POST.get('description')
            date_expiration= request.POST.get('date_expiration')
            Image= request.FILES.get('image')

            if not name:
                 errors['name']="le nom est requis"


            if not category_id:
                 errors['category']="la categorie est requise"

            if not price :
                 errors['price']= "le prix est requis"

            if not quantite:
                 errors['quantite']= "la quantite est requis" 

            if not description:
                 errors['description']= "la description est requise"

            if date_expiration:

                 try:
                      datetime.strftime(date_expiration, '%Y-%m-%d')  
                 except ValueError:
                      errors['date_expiration']= "le format de la date d'expiration est incorect" 



            if not errors:
                 
                 category= get_object_or_404(Categories, id= category_id)
                 produit.name= name
                 produit.category= category
                 produit.price=price
                 produit.quantite= quantite
                 produit.description=description
                 produit.date_expiration=date_expiration



                 if image:
                      fs= FileSystemStorage()
                      filname= fs.save(name.name, image)

                      produit.image = fs.url(filname)



            produit.save()
            messages.success(request, "le produit a été modifié avec succés!")
            return redirect("home")
       
       else:
            

            for key, error in errors.items():
                 
                 messages.error(request, error)

       return render (request, "modification.html",{'produit': produit, 'categories': categories, 'errors':errors})    
                 
            

                 

                 
                        





 





            




#def ajout_donnees(request):
 #   if request.method == 'POST' :
  #      name= request.POST['name']
   #     price= request.POST['price']
    #    quantite= request.POST['quantite']
     #   description=request.POST['description']
      #  date_expiration= request.POST['date_expiration']
       # image= request.FILES['image']

        #category = Categories.objects.get(pk=request.POST['category'])
        #savedonnes= Produits(name=name, price=price, quantite= quantite,description =description ,date_expiration=date_expiration,category=category, image=image)
       # savedonnes.save()
       # return redirect('home')

                             


    #else:
     #   category= Categories.objects.all()

    
    #return render(request, "ajout_donnees.html",{"category":category})


