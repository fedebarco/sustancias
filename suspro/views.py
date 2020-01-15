from django.http import HttpResponse,JsonResponse
import CoolProp.CoolProp as CP


def saludo(request):
    return HttpResponse("Hola perro")

def Calculaentalpia(request,temperatura,presion):
    periodo=CP.PropsSI('H','T',temperatura,'P',presion,'Water')
    return JsonResponse({'entalpia':periodo})
def objetoJ(request):
    casa='5'
    return JsonResponse({'casa':casa})
