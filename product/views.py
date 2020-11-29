from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone
 
x=0

# Create your views here.

def home(request):
    productss=product.objects.all()
    return render (request,'products/home.html',{'abb':productss})
    



@login_required
def Create(request):

    if request.method=='POST':
    
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image'] :

            product_in=product()
            product_in.title=request.POST['title']
            product_in.body=request.POST['body']
            product_in.icon=request.FILES['icon']
            product_in.image=request.FILES['image']
            
            product_in.url=request.POST['url']
            product_in.hunter=request.user
            product_in.pub_date=timezone.datetime.now()
            product_in.save()
            return redirect('/product/'+str(product_in.id))
        else:

            return render (request,'products/create.html')



    else:

         return render (request,'products/create.html')



def Pdetails(request,productid):
    obj = get_object_or_404(product, pk=productid)
    
   
    return render(request,'products/details.html',{'obj':obj})



@login_required
def upvote (request , productid ):
    if request.method=='POST':
        obj = get_object_or_404(product, pk=productid)
        obj.votes_total +=1
        obj.save()
        return redirect('/product/'+str(obj.id))


   

       





           

    
 