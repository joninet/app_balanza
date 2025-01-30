from flask import Flask, render_template, session, redirect, url_for, request
app = Flask(__name__)
app.secret_key = "una_clave_secreta"

# Variable de peso fijo
PESO_FIJO = float(2.5)

productos = [
    {
        "id": 1, 
        "nombre": "Arandanos", 
        "precio": 200,
        "imagen": "static/images/arandanos.jpeg"
    },
    {
        "id": 2, 
        "nombre": "Banana", 
        "precio": 150,
        "imagen": "static/images/banana.jpeg"
    },
    {
        "id": 3, 
        "nombre": "Naranja", 
        "precio": 180,
        "imagen": "static/images/naranja.jpeg"
    },
    {
        "id": 4, 
        "nombre": "Pera", 
        "precio": 220,
        "imagen": "static/images/pera.jpeg"
    },
        {
        "id": 1, 
        "nombre": "Arandanos", 
        "precio": 200,
        "imagen": "static/images/arandanos.jpeg"
    },
    {
        "id": 2, 
        "nombre": "Banana", 
        "precio": 150,
        "imagen": "static/images/banana.jpeg"
    },
    {
        "id": 3, 
        "nombre": "Naranja", 
        "precio": 180,
        "imagen": "static/images/naranja.jpeg"
    },
    {
        "id": 4, 
        "nombre": "Pera", 
        "precio": 220,
        "imagen": "static/images/pera.jpeg"
    }
    
]

@app.route("/")
def index():
    return render_template("index.html", productos=productos, peso_fijo=PESO_FIJO)

@app.route("/agregar", methods=["POST"])
def agregar():
    producto_id = int(request.form["id"])
    
    # Usar el peso fijo en lugar del formulario
    peso = PESO_FIJO

    if "carrito" not in session:
        session["carrito"] = []

    producto = next((p for p in productos if p["id"] == producto_id), None)
    
    if producto:
        item = {
            "nombre": producto["nombre"],
            "peso": peso,
            "precio_unitario": producto["precio"],
            "total": producto["precio"] * peso,
        }
        session["carrito"].append(item)
        session.modified = True
        return redirect(url_for("index"))
    return "Producto no encontrado", 404


@app.route("/carrito")
def ver_carrito():
    carrito = session.get("carrito", [])
    total = sum(item["total"] for item in carrito)
    return render_template("carrito.html", carrito=carrito, total=total)

@app.route("/limpiar")
def limpiar_carrito():
    session.pop("carrito", None)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
