from django.http import HttpResponse
from django.template import Template, Context
from gestion.models import productos,categoria

def productos_lista(request):
    productos_l = productos.objects.all()
    document=open(r'D:\Esteban\Demon\evalucion_env\ecommerce\Templates\Productos.html')
    plt=Template(document.read())
    document.close()
    cxt=Context({
        "productos_lista":productos_l
    })
    document=plt.render(cxt)
    return HttpResponse(document)

def categoria_lista(request):
    categoria_l = categoria.objects.all()
    document=open(r"D:\Esteban\Demon\evalucion_env\ecommerce\Templates\categoria.html")
    plt=Template(document.read())
    document.close()
    cxt=Context({
        "categoria_lista":categoria_l
        })
    document=plt.render(cxt)
    return HttpResponse(document)
