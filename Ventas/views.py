# encoding:utf-8
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Cliente
from .forms import ClientForm

# Create your views here.


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


"""def client_new(request):
        form = ClientForm()
        return render(request, 'Ventas/client_edit.html', {'form': form})
"""
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




def home(request):
	#return render(request,'login2.html')
    return HttpResponse("Hello, world. You're at the polls index.")


def inicio(request):
	#return render(request,'login2.html')
    return HttpResponse("Hello, world. You're at the polls indexdjfkdjfkdjfkdjf.")


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