
from flask import Flask, render_template, abort

app = Flask(__name__)


CATEGORIES = {
    "camisetas": {
        "name": "Camisetas",
        "eyebrow": "ESSENCIAIS DO DIA A DIA",
        "description": "Modelagens versáteis e detalhes que fazem a diferença.",
        "has_size_filter": True,
        "sizes": ["P", "M", "G", "GG", "G1", "G2", "G3"],
        "products": [
            "Camiseta Branca A|X",
            "Camiseta Branca Dunlop",
            "Camiseta Bege Tommy Hilfiger",
            "Camiseta Verde Levi's",
            "Camiseta Verde Ellus",
            "Camiseta Verde Aramis",
            "Camiseta Verde Calvin Klein",
            "Camiseta Verde Tommy Hilfiger",
            "Camiseta Verde Claro Ralph Lauren",
            "Camiseta Verde Ralph Lauren",
            "Camiseta Amarelo Ralph Lauren",
            "Camiseta Azul Boss",
            "Camiseta Vermelha Boss",
            "Camiseta Vermelha Ralph Lauren",
            "Camiseta Cinza Armani"
        ]
    },
    "camisas": {
        "name": "Camisas",
        "eyebrow": "ELEGÂNCIA EM CADA DETALHE",
        "description": "Peças que transitam entre ocasiões com naturalidade.",
        "has_size_filter": False,
        "sizes": [],
        "products": [
            "Camisa Classic",
            "Camisa Linen",
            "Camisa Urban",
            "Camisa Premium"
        ]
    },
    "calcas": {
        "name": "Calças",
        "eyebrow": "CAIMENTO E PERSONALIDADE",
        "description": "Silhuetas contemporâneas e conforto.",
        "has_size_filter": True,
        "sizes": list(range(38, 54, 2)),
        "products": [
            "Calça Tailored",
            "Calça Straight",
            "Calça Relaxed",
            "Calça Essential"
        ]
    },
    "bermudas": {
        "name": "Bermudas",
        "eyebrow": "LEVEZA E VERSATILIDADE",
        "description": "Conforto e estilo para diferentes ocasiões.",
        "has_size_filter": True,
        "sizes": list(range(38, 50, 2)),
        "products": [
            "Bermuda Casual",
            "Bermuda Urban",
            "Bermuda Essential",
            "Bermuda Relaxed"
        ]
    },
    "bones": {
        "name": "Bonés",
        "eyebrow": "O DETALHE FINAL",
        "description": "Acessórios que completam sua composição.",
        "has_size_filter": False,
        "sizes": [],
        "products": [
            "Boné Classic",
            "Boné Minimal",
            "Boné Signature",
            "Boné Everyday"
        ]
    },
    "perfumes": {
        "name": "Perfumes",
        "eyebrow": "UMA ASSINATURA INESQUECÍVEL",
        "description": "Fragrâncias para expressar sua presença.",
        "has_size_filter": False,
        "sizes": [],
        "products": [
            "Essence Nº 01",
            "Essence Nº 02",
            "Signature Nº 01",
            "Signature Nº 02"
        ]
    }
}


COLORS = [
    {"name": "Preto", "hex": "#171717"},
    {"name": "Branco", "hex": "#F5F5F2"},
    {"name": "Cinza", "hex": "#929292"},
    {"name": "Bege", "hex": "#C8B99F"},
    {"name": "Marrom", "hex": "#76543B"},
    {"name": "Azul", "hex": "#263D62"},
    {"name": "Verde", "hex": "#53634D"}
]


def format_price(price):
    return (
        f"R$ {price:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def create_products(category_data, category_slug):

    products = []

    for index, name in enumerate(category_data["products"]):

        # =====================================
        # CAMISETAS PERSONALIZADAS
        # =====================================

        if category_slug == "camisetas" and index == 0:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-branca-ax-p-frente.png",
                    "alt": "Camiseta Branca A|X - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-branca-ax-p-costas.png",
                    "alt": "Camiseta Branca A|X - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-branca-ax-p",
                "name": "Camiseta Branca A|X",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Branco",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue

        # =====================================
        # CAMISETA DUNLOP
        # =====================================

        if category_slug == "camisetas" and index == 1:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-branca-dunlop-p-frente.png",
                    "alt": "Camiseta Branca Dunlop - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-branca-dunlop-p-costas.png",
                    "alt": "Camiseta Branca Dunlop - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-branca-dunlop-p",
                "name": "Camiseta Branca Dunlop",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Branco",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })
            
            continue
        
        if category_slug == "camisetas" and index == 2:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-bege-tommy-p-frente.png",
                    "alt": "Camiseta Bege Tommy Hilfiger - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-bege-tommy-p-costas.png",
                    "alt": "Camiseta Bege Tommy Hilfiger - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-bege-tommy-hilfiger-p",
                "name": "Camiseta Bege Tommy Hilfiger",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Bege",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        if category_slug == "camisetas" and index == 3:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-verde-levis-p-frente.png",
                    "alt": "Camiseta Verde Levi's - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-verde-levis-p-costas.png",
                    "alt": "Camiseta Verde Levi's - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-verde-levis-p",
                "name": "Camiseta Verde Levi's",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Verde",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # CAMISETA ELLUS
        # =====================================

        if category_slug == "camisetas" and index == 4:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-verde-ellus-p-frente.png",
                    "alt": "Camiseta Verde Ellus - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-verde-ellus-p-costas.png",
                    "alt": "Camiseta Verde Ellus - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-verde-ellus-p",
                "name": "Camiseta Verde Ellus",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Verde",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # CAMISETA ARAMIS
        # =====================================

        if category_slug == "camisetas" and index == 5:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-verde-aramis-p-frente.png",
                    "alt": "Camiseta Verde Aramis - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-verde-aramis-p-costas.png",
                    "alt": "Camiseta Verde Aramis - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-verde-aramis-p",
                "name": "Camiseta Verde Aramis",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Verde",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # CAMISETA CALVIN KLEIN
        # =====================================

        if category_slug == "camisetas" and index == 6:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-verde-calvin-p-frente.png",
                    "alt": "Camiseta Verde Calvin Klein - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-verde-calvin-p-costas.png",
                    "alt": "Camiseta Verde Calvin Klein - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-verde-calvin-klein-p",
                "name": "Camiseta Verde Calvin Klein",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Verde",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # CAMISETA TOMMY HILFIGER VERDE
        # =====================================

        if category_slug == "camisetas" and index == 7:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-verde-tommy-p-frente.png",
                    "alt": "Camiseta Verde Tommy Hilfiger - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-verde-tommy-p-costas.png",
                    "alt": "Camiseta Verde Tommy Hilfiger - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-verde-tommy-hilfiger-p",
                "name": "Camiseta Verde Tommy Hilfiger",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Verde",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # CAMISETA RALPH LAUREN VERDE CLARO
        # =====================================

        if category_slug == "camisetas" and index == 8:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-verde-claro-ralph-p-frente.png",
                    "alt": "Camiseta Verde Claro Ralph Lauren - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-verde-claro-ralph-p-costas.png",
                    "alt": "Camiseta Verde Claro Ralph Lauren - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-verde-claro-ralph-lauren-p",
                "name": "Camiseta Verde Claro Ralph Lauren",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Verde claro",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # CAMISETA RALPH LAUREN VERDE
        # =====================================

        if category_slug == "camisetas" and index == 9:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-verde-ralph-p-frente.png",
                    "alt": "Camiseta Verde Ralph Lauren - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-verde-ralph-p-costas.png",
                    "alt": "Camiseta Verde Ralph Lauren - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-verde-ralph-lauren-p",
                "name": "Camiseta Verde Ralph Lauren",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Verde",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # CAMISETA CALVIN KLEIN AMARELA
        # =====================================

        if category_slug == "camisetas" and index == 10:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-amarela-calvin-p-frente.png",
                    "alt": "Camiseta Amarela Calvin Klein - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-amarela-calvin-p-costas.png",
                    "alt": "Camiseta Amarela Calvin Klein - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-amarela-calvin-klein-p",
                "name": "Camiseta Amarela Calvin Klein",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Amarelo",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # CAMISETA AZUL BOSS
        # =====================================

        if category_slug == "camisetas" and index == 11:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-azul-boss-p-frente.png",
                    "alt": "Camiseta Azul BOSS - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-azul-boss-p-costas.png",
                    "alt": "Camiseta Azul BOSS - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-azul-boss-p",
                "name": "Camiseta Azul BOSS",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Azul",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # CAMISETA BOSS VERMELHA
        # =====================================

        if category_slug == "camisetas" and index == 12:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-vermelha-boss-p-frente.png",
                    "alt": "Camiseta Vermelha BOSS - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-vermelha-boss-p-costas.png",
                    "alt": "Camiseta Vermelha BOSS - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-vermelha-boss-p",
                "name": "Camiseta Vermelha BOSS",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Vermelho",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
    
        # =====================================
        # CAMISETA RALPH LAUREN VERMELHA
        # =====================================

        if category_slug == "camisetas" and index == 13:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-vermelha-ralph-p-frente.png",
                    "alt": "Camiseta Vermelha Ralph Lauren - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-vermelha-ralph-p-costas.png",
                    "alt": "Camiseta Vermelha Ralph Lauren - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-vermelha-ralph-lauren-p",
                "name": "Camiseta Vermelha Ralph Lauren",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Vermelho",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
            # =====================================
            # CAMISETA ARMANI CINZA
            # =====================================

        if category_slug == "camisetas" and index == 14:

            price = 100.00

            images = [
                {
                    "src": "images/products/camiseta-cinza-armani-p-frente.png",
                    "alt": "Camiseta Cinza Armani - Frente",
                    "label": "Frente"
                },
                {
                    "src": "images/products/camiseta-cinza-armani-p-costas.png",
                    "alt": "Camiseta Cinza Armani - Costas",
                    "label": "Costas"
                }
            ]

            products.append({
                "slug": "camiseta-cinza-armani-p",
                "name": "Camiseta Cinza Armani",
                "category": category_data["name"],
                "price": price,
                "price_label": format_price(price),
                "color": "Cinza",
                "sizes": category_data["sizes"],
                "discount": 0,
                "is_new": True,
                "tag": "NOVO",
                "image": images[0]["src"],
                "images": images
            })

            continue
        
        # =====================================
        # DEMAIS PRODUTOS
        # =====================================

        price = 149.90 + (index * 50)

        products.append({
            "slug": f"{category_slug}-{index + 1}",
            "name": name,
            "category": category_data["name"],
            "price": price,
            "price_label": format_price(price),
            "color": COLORS[index % len(COLORS)]["name"],
            "sizes": category_data["sizes"],
            "discount": 10 if index == 0 else 0,
            "is_new": index == 0,
            "tag": "NOVO" if index == 0 else "",
            "image": None,
            "images": []
        })

    return products

def get_all_products():

    products = []

    for category_slug, category_data in CATEGORIES.items():
        products.extend(
            create_products(category_data, category_slug)
        )

    return products


@app.context_processor
def inject_categories():

    return {
        "nav_categories": [
            {
                "slug": slug,
                "name": data["name"]
            }
            for slug, data in CATEGORIES.items()
        ]
    }


@app.route("/")
def home():

    products = [
        {
            "name": "Peça essencial 01",
            "category": "Coleção essencial",
            "price": "R$ 0,00",
            "tag": "NOVO",
            "image": None
        },
        {
            "name": "Peça essencial 02",
            "category": "Coleção essencial",
            "price": "R$ 0,00",
            "tag": "",
            "image": None
        },
        {
            "name": "Peça essencial 03",
            "category": "Coleção essencial",
            "price": "R$ 0,00",
            "tag": "DESTAQUE",
            "image": None
        },
        {
            "name": "Peça essencial 04",
            "category": "Coleção essencial",
            "price": "R$ 0,00",
            "tag": "",
            "image": None
        }
    ]

    return render_template(
        "index.html",
        products=products
    )


@app.route("/categoria/<slug>")
def category(slug):

    category_data = CATEGORIES.get(slug)

    if category_data is None:
        abort(404)

    products = create_products(category_data, slug)

    return render_template(
        "category.html",
        category=category_data,
        products=products,
        active_slug=slug,
        has_size_filter=category_data["has_size_filter"],
        sizes=category_data["sizes"],
        colors=COLORS
    )


@app.route("/produto/<slug>")
def product_detail(slug):

    products = get_all_products()

    product = next(
        (item for item in products if item["slug"] == slug),
        None
    )

    if product is None:
        abort(404)

    return render_template(
        "product.html",
        product=product
    )


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)