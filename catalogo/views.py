from django.shortcuts import render
from urllib.parse import quote

def landing_catalogo(request):
    productos = [
        {
            "nombre": "Camiseta DryFit Sportline",
            "descripcion": "Tela ligera, de secado rápido, ideal para gym y running.",
            "precio": "$14.99",
            "categoria": "Running",
            "color": "Azul / Negro",
            "talla": "S, M, L, XL",
            "imagen": "catalogo/camiseta.png",
        },
        {
            "nombre": "Leggins de Compresión Sportline",
            "descripcion": "Mayor soporte muscular para entrenamientos intensos.",
            "precio": "$19.99",
            "categoria": "Gym",
            "color": "Negro",
            "talla": "S, M, L",
            "imagen": "catalogo/leggins.png",
        },
        {
            "nombre": "Short Pro Training",
            "descripcion": "Corte cómodo y ligero.",
            "precio": "$12.99",
            "categoria": "Training",
            "color": "Gris / Negro",
            "talla": "M, L, XL",
            "imagen": "catalogo/short.png",
        },
        {
            "nombre": "Sudadera Ligera Sportline",
            "descripcion": "Perfecta para antes y después de entrenar.",
            "precio": "$24.99",
            "categoria": "Casual Deportivo",
            "color": "Gris",
            "talla": "S, M, L, XL",
            "imagen": "catalogo/sudadera.png",
        },
    ]

    numero = "50360262769"  

    productos_final = []
    for p in productos:
        msg = quote(f"Hola, quiero más información sobre: {p['nombre']}")
        wa_link = f"https://wa.me/{numero}?text={msg}"
        productos_final.append({**p, "whatsapp": wa_link})

    return render(request, "landing_productos.html", {
        "productos": productos_final,
        "titulo": "Sportline - Ropa Deportiva",
        "slogan": "Activa tu mejor versión.",
    })
