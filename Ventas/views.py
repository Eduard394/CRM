from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Cliente
# Create your views here.


def post_list(request):
	clientes_list = Cliente.objects.filter(fecha_crea__lte=timezone.now()).order_by('nombres')
        return render(request, 'Ventas/post_list.html', {'clientes_list': clientes_list})





def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")