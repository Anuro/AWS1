# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import MyModel

def create_data(request):
    if request.method == 'POST':
        data = request.POST.get('data')
        my_model_instance = MyModel()
        my_model_instance.set_data(data)
        my_model_instance.save()
        return HttpResponse('Datos cifrados y almacenados correctamente.')
    return render(request, 'create_data.html')

def get_data(request, pk):
    my_model_instance = MyModel.objects.get(pk=pk)
    decrypted_data = my_model_instance.get_data()
    return HttpResponse(f'Datos descifrados: {decrypted_data}')
