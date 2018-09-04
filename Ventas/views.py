# encoding:utf-8
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from .models import Cliente,Producto,Venta
from .forms import ClientForm,NewVentaForm,ProductoForm,VentaForm
from django.views.generic import CreateView, ListView,TemplateView

# Create your views here.

### INICIOOO####################################

def home(request):
    return render(request,'Ventas/home.html')
    #return HttpResponse("Hello, world. You're at the polls index.")


def inicio(request):
    #return render(request,'Ventas/home.html')
    return HttpResponse("Hello, world. You're at the polls indexdjfkdjfkdjfkdjf.")











######## INICIO Clientes ####################

def client_list(request):
	clientes_list = Cliente.objects.filter(fecha_crea__lte=timezone.now()).order_by('nombres')
        return render(request, 'Ventas/client_list.html', {'clientes_list': clientes_list})


def client_detail(request,pk):
	cliente_detail = get_object_or_404(Cliente, pk=pk)
    	return render(request, 'Ventas/client_detail.html', {'cliente_detail': cliente_detail})

def client_new(request):
	if request.method == "POST":
		form = ClientForm(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			client.fecha_crea = timezone.now()
			client.save()
			return redirect('client_detail', pk=client.pk)
	else:
		form=ClientForm()
		return render(request,'Ventas/client_edit.html', {'form': form})

def client_edit(request, pk):
        client = get_object_or_404(Cliente, pk=pk)
        if request.method == "POST":
            form = ClientForm(request.POST, instance=client)
            if form.is_valid():
                client = form.save(commit=False)
                client.fecha_crea = timezone.now()
                client.save()
                return redirect('client_detail', pk=client.pk)
        else:
            form = ClientForm(instance=client)
        return render(request, 'Ventas/client_edit.html', {'form': form})
###### FIN Clientes ####################


###### Inicio Productos ####################

def producto_list(request):
        productos_list = Producto.objects.all().order_by('nombre')
        return render(request, 'Ventas/producto_list.html', {'productos_list': productos_list})

def producto_detail(request,pk):
        producto_detail = get_object_or_404(Producto, pk=pk)
        return render(request, 'Ventas/producto_detail.html', {'producto_detail': producto_detail})

def producto_new(request):
    if request.method=="POST":
        form=ProductoForm(request.POST)
        if form.is_valid():
            producto=form.save(commit=False)
            producto.save()
            return redirect('producto_detail', pk=producto.pk)
    else:
        form=ProductoForm()

    return render(request,'Ventas/producto_edit.html',{'form': form})
    #return HttpResponse("Hello, world. You're at the polls indexdjfkdjfkdjfkdjf.")
def producto_edit(request, pk):
        producto = get_object_or_404(Producto, pk=pk)
        if request.method == "POST":
            form = ProductoForm(request.POST, instance=producto)
            if form.is_valid():
                producto = form.save(commit=False)
                producto.fecha_crea = timezone.now()
                producto.save()
                return redirect('producto_detail', pk=producto.pk)
        else:
            form = ProductoForm(instance=producto)
        return render(request, 'Ventas/producto_edit.html', {'form': form})

###### FIN Productos ####################


#### Inicio Venta ############

def venta_new(request):
    if request.method=="POST":
        form=VentaForm(request.POST)
        if form.is_valid():
            venta=form.save(commit=False)
            venta.save()
            return redirect('venta_detail', pk=venta.pk)
    else:
        form=VentaForm()

    return render(request,'Ventas/venta_edit.html',{'form': form})
    #return HttpResponse("Hello, world. You're at the polls indexdjfkdjfkdjfkdjf.")


def venta_edit(request, pk):
        venta = get_object_or_404(Venta, pk=pk)
        if request.method == "POST":
            form = VentaForm(request.POST, instance=venta)
            if form.is_valid():
                venta= form.save(commit=False)
                venta.fecha = timezone.now()
                venta.save()
                return redirect('venta_detail', pk=venta.pk)
        else:
            form = VentaForm(instance=venta)
        return render(request, 'Ventas/venta_edit.html', {'form': form})



def venta_detail(request,pk):
        venta_detail = get_object_or_404(Venta, pk=pk)
        return render(request, 'Ventas/venta_detail.html', {'venta_detail': venta_detail})



def venta_list(request):
        venta_list = Venta.objects.all().order_by('fecha')
        return render(request, 'Ventas/venta_list.html', {'venta_list': venta_list})

"""def venta_edit(request, pk):
        venta = get_object_or_404(Venta pk=pk)
        if request.method == "POST":
            form = VentaForm(request.POST, instance=venta)
            if form.is_valid():
                venta = form.save(commit=False)
                venta.fecha = timezone.now()
                venta.save()
                return redirect('venta_detail', pk=venta.pk)
        else:
            form = VentaForm(instance=venta)
        return render(request, 'Ventas/venta_edit.html', {'form': form})
"""


class NewActividad(CreateView):
    model = Venta
    template_name = "Ventas/newVenta.html"
    form_class = NewVentaForm
    success_url = reverse_lazy('Ventas/client_list.html')

###### FIN Venta ################


"""def login_(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)

                else:
                    messages.error(request, (
                        'No esta autorizado para ingresar a la plataforma'))
                    return redirect(reverse('inicio', args=()))
            else:
                messages.error(request, (
                    'El usuario o la contraseña son incorrectos'))
                return redirect(reverse('inicio', args=()))
    return redirect('inicio')
"""