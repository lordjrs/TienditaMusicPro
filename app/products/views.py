from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product,Category
from .forms import PoleraForm
from cart.cart import Cart
from rest_framework import viewsets
from app.serializers import ProductoSerializer,CategorySerializer

# Create your views here.

class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductoSerializer
    
    def get_queryset(self):
        productos = Product.objects.all()
        name = self.request.GET.get('name')
        
        if name:
            productos = productos.filter(name__contains=name)
        return productos

@login_required(login_url='/autenticacion/acceder')
def listado_productos(request):
    cart = Cart(request)
    products = Product.objects.all()
    return render(request, "products/listado.html", {
        "products": products
    })
    
def read(request):
    producto = Product.objects.all()
    return render(request, "products/read.html", {
        "poleras": producto
    })
    
def agregar(request):

    data = {
        'form':PoleraForm()
    }
    
    if request.method == 'POST':
        formulario = PoleraForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['msg'] = "Guardado de forma exitosa."
            
    return render(request, "products/agregar.html", data)

def eliminar(request, id):
    polera = Product.objects.get(id=id)
    polera.delete()
    return redirect(to="read")