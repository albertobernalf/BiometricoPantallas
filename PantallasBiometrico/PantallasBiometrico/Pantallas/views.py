from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, TemplateView, View
import requests
import json
from django.http import HttpResponse, JsonResponse

# Create your views here.

class salidaView(TemplateView):
    print("Entre Inicio5")
    template_name = 'salida.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi Inicio'

        return context

    def post(self, request, *args, **kwargs):
        print("Entre POST salida.html")

        codigo = request.POST.get('codigo')
        nombre = request.POST.get('nombre')
        acceso = request.POST.get('acceso')
        print(codigo)
        print(nombre)
        print(acceso)
        datos = {}
        context = {}
        datos['codigo'] = codigo
        datos['nombre'] = nombre
        datos['acceso'] = acceso

        print(datos['codigo'])

        if datos['codigo'] == '0':
            print("Opcion 0")
            return render(request, 'inicio4.html', context)

        if datos['codigo'] == '1':
            print("Opcion 1")
            context['nombre'] = datos['nombre']
            return render(request, 'inicio5.html', context)

        if datos['codigo'] == '2':
            print("Opcion 2")
            return render(request, 'inicio6.html', context)


def data1(request):

    url = "http://jacgsaw.com/siath/app/war"
    datos = {'app_key' : 'jac2021-791' , 'id_pi' : '10', 'rf_id':'060060B37DA8'}
    response = requests.post(url, data=datos)

    if response.status_code == 200:
        print(response.text)
        resultado0 = response.text
        json_dic = json.loads (resultado0)
        print("json_dic : " , json_dic)
        print(json_dic["id"])
        print(json_dic["name"])
        print(json_dic["sys"])
        print(json_dic["sys"]["var0"])
        print(json_dic["sys"]["var1"])
        print(json_dic["sys"]["var2"])
        print(json_dic["sys"]["var3"])

    context = {}
    # Pruebas
    json_dic["id"] = 0
    json_dic["name"] = "Ing. Alexander Cruz"

    if json_dic["id"]  == 0:
        print("Opcion 0")
        return render(request, 'inicio4.html', context)

    if json_dic["id"] == 1:
        print("Opcion 1")
        context['id_pi'] = json_dic["name"]
        return render(request, 'inicio5.html', context)

    if json_dic["id"] == 2:
        print("Opcion 2")
        return render(request, 'inicio6.html', context)


