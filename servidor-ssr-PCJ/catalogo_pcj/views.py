from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]

# "Base de datos" falsa: una lista de diccionarios en memoria.
# En un proyecto real esto vendria de un modelo (models.py) y una tabla,
# pero para ENTENDER que es SSR no necesitamos base de datos: lo importante
# es que estos datos se insertan en el HTML *antes* de enviarlo al navegador.
PRODUCTOS = [
    {"nombre": "Playera UT Hermosillo", "precio": 250, "stock": 40},
    {"nombre": "Sudadera TIC", "precio": 480, "stock": 15},
    {"nombre": "Taza PWA", "precio": 120, "stock": 60},
    {"nombre": "Mochila 10mo cuatrimestre", "precio": 690, "stock": 8},
]


def vista_ssr(request):
    """
    Vista con Renderizado en Servidor (SSR).

    request: el objeto que representa la peticion que hizo el navegador.

    render() hace tres cosas:
      1) toma la plantilla 'catalogo/catalogo_ssr.html'
      2) le inyecta el diccionario de "contexto" (aqui: la lista de productos)
      3) devuelve el HTML final, YA CON LOS DATOS DENTRO, listo para el navegador.

    Por eso es "servidor": el HTML que llega al navegador ya trae escritos
    los nombres y precios. Si haces clic derecho > "Ver codigo fuente de la
    pagina" veras los productos en el HTML, aunque JavaScript este desactivado.
    Comparalo con la vista CSR de la Parte B, donde el HTML llega vacio y es
    JavaScript quien dibuja los productos DESPUES, ya en el navegador.
    """
    contexto = {"productos": PRODUCTOS}
    return render(request, 'catalogo/catalogo_ssr.html', contexto)
