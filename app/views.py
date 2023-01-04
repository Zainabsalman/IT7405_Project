from django.shortcuts import HttpResponseRedirect, render, redirect
from app.models import App 
from app.functions import handle_uploaded_file
from app.forms import routerForm
from django.http import HttpResponseRedirect

# Create your views here.
def app_list(request):
    app_objects =   App.objects.all()
    return render(request, 'base.html', {"app_objects": app_objects})

def app_details(request, id):
    app_item= App.objects.get(id=id)
    return render(request, 'details.html', {'app_item':app_item})

def addRouter(request):
    myForm = routerForm
    if request.method == "POST":
        myForm = routerForm(request.POST, request.FILES)
        if myForm.is_valid():
            handle_uploaded_file(request.FILES['image']) ##image is the name of the filed that has the image file
            name = myForm.cleaned_data["name"]
            brand = myForm.cleaned_data["brand"]
            model = myForm.cleaned_data["model"]
            description = myForm.cleaned_data["description"]
            imageFileName = request.FILES['image'].name
            imagePath = "app/img/{0}".format(imageFileName) ## should be same as path you did in function
            AppObj = App(name=name,brand=brand,model=model,description=description,image=imagePath)
            AppObj.save()
            
        return HttpResponseRedirect("/")
    return render(request, 'addRouter.html', {"myForm": myForm})

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        device = App.objects.filter(name__contains=searched)
        return render(request,"search.html",{'searched': searched, 'device': device})
    else:
      return render(request,"search.html")  

def update(request, id):
    device = App.objects.get(id=id)

    if request.method == 'POST':
        device.name = request.POST["name"]
        device.brand = request.POST["brand"]
        device.model = request.POST["model"]
        device.description = request.POST["description"]

        if len(request.FILES) != 0:
            imageFileName = request.FILES['image'].name
            imagePath = "app/img/{0}".format(imageFileName) ## should be same as path you did in function
            handle_uploaded_file(request.FILES['image'])
            device.image = imagePath

        device.save()

        return HttpResponseRedirect("/")
    return render(request,'update.html',{'device': device})

def delete(request, id):
    device = App.objects.get(id=id)
    device.delete()
    return redirect('app:homepage')
    