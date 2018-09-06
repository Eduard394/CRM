# encoding:utf-8
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from .models import Cliente,Producto,Venta
from .forms import ClientForm,NewVentaForm,ProductoForm,VentaForm,NewClientForm,NewProductoForm

from django.views.generic import CreateView, ListView,TemplateView,UpdateView,DeleteView

############## Vistas Basadas en Funciones#############


def home(request):
    return render(request,'Ventas/home.html')
    #return HttpResponse("Hello, world. You're at the polls index.")


def inicio(request):
    #return render(request,'Ventas/home.html')
    return HttpResponse("Hello, world. You're at the polls indexdjfkdjfkdjfkdjf.")


######## INICIO Clientes ####################

def client_list(request):
	clientes_list = Cliente.objects.filter(fecha_crea__lte=timezone.now()).order_by('nombres')
        return render(request, 'Clientes/client_list.html', {'clientes_list': clientes_list})


def client_detail(request,pk):
	cliente_detail = get_object_or_404(Cliente, pk=pk)
    	return render(request, 'Clientes/client_detail.html', {'cliente_detail': cliente_detail})

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
		return render(request,'Clientes/client_edit.html', {'form': form})

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
        return render(request, 'Clientes/client_edit.html', {'form': form})
###### FIN Clientes ####################


###### Inicio Productos ####################

def producto_list(request):
        productos_list = Producto.objects.all().order_by('nombre')
        return render(request, 'Productos/producto_list.html', {'productos_list': productos_list})

def producto_detail(request,pk):
        producto_detail = get_object_or_404(Producto, pk=pk)
        return render(request, 'Productos/producto_detail.html', {'producto_detail': producto_detail})

def producto_new(request):
    if request.method=="POST":
        form=ProductoForm(request.POST)
        if form.is_valid():
            producto=form.save(commit=False)
            producto.save()
            return redirect('producto_detail', pk=producto.pk)
    else:
        form=ProductoForm()

    return render(request,'Productos/producto_edit.html',{'form': form})

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
        return render(request, 'Productos/producto_edit.html', {'form': form})

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

##############  FIN Vistas Basadas en Funciones #############


############## Vistas Basadas en clases #############

######### clases para clientes #########

class Cliente_list(ListView):
    model= Cliente
    template_name='Clientes/client_list_class.html'



class Cliente_create(CreateView):
    model = Cliente
    form_class = NewClientForm
    template_name = 'Clientes/client_edit_class.html'
    success_url = reverse_lazy('client_listar')

    def form_valid(self, form):
        form.instance.activo = True
        return super(Cliente_create, self).form_valid(form)


class Cliente_edit(UpdateView):
    model = Cliente
    form_class = NewClientForm
    template_name = 'Clientes/client_edit_class.html'
    success_url = reverse_lazy('client_listar')


class Cliente_delete(DeleteView):
    model = Cliente
    form_class = NewClientForm
    template_name = 'Clientes/client_delete.html'
    success_url = reverse_lazy('client_listar')


######### FIN clases para clientes #########


######### clases para Productos #########

class Producto_list(ListView):
    model= Producto
    template_name='Productos/producto_list_class.html'

class Producto_create(CreateView):
    model = Producto
    form_class = NewProductoForm
    template_name = 'Productos/producto_edit_class.html'
    success_url = reverse_lazy('producto_listar')

    def form_valid(self, form):
        return super(Producto_create, self).form_valid(form)

class Producto_edit(UpdateView):
    model = Producto
    form_class = NewProductoForm
    template_name = 'Productos/producto_edit_class.html'
    success_url = reverse_lazy('producto_listar')

class Producto_delete(DeleteView):
    model = Producto
    form_class = NewProductoForm
    template_name = 'Productos/producto_delete.html'
    success_url = reverse_lazy('producto_listar')

######### FIN clases para Productos #########


######### clases para Ventas #########

class Venta_list(ListView):
    model= Venta
    template_name='Ventas/venta_list_class.html'

class Venta_create(CreateView):
    model = Venta
    form_class = NewVentaForm
    template_name = 'Ventas/venta_edit_class.html'
    success_url = reverse_lazy('venta_list')

    def form_valid(self, form):
        return super(Venta_create, self).form_valid(form)

class Venta_edit(UpdateView):
    model = Venta
    form_class = NewVentaForm
    template_name = 'Ventas/venta_edit_class.html'
    success_url = reverse_lazy('venta_list')

class Venta_delete(DeleteView):
    model = Venta
    form_class = NewVentaForm
    template_name = 'Ventas/venta_delete.html'
    success_url = reverse_lazy('venta_list')

######### FIN clases para Ventas #########





##############   Fin Vistas Basadas en clases #############