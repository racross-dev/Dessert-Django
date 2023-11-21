from django.shortcuts import render
# from django.http import HttpResponse
import requests

# Create your views here.


def index(request):
    return render(request, 'index.html')


def sobre_nosotros(request):
    return render(request, 'sobre_nosotros.html')


def contacto(request):
    return render(request, 'contacto.html')


def colecciones(request):
    return render(request, 'colecciones.html')


def top(request):
    url = "http://localhost:3000/productos/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.HTTPError as errh:
        print("Http Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("OOps: Something went wrong", err)

    return render(request, 'top.html', {'productos': data})
