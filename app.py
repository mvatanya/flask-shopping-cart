"""Shopping cart application."""

from flask import Flask, request, session, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from products import Product

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def homepage():
    """Homepage: show list of products with link to product page."""
    products = Product.get_all()
    return render_template("homepage.html", products=products)

@app.route("/products/<int:product_id>")
def product_detail(product_id):
    """Show detail of product, along with add-to-cart form."""
    product_id = Product.get_by_id(product_id)
    return render_template("product.html", product_id=product_id)

@app.route("/cart")
def show_cart():
    """Show shopping cart."""
    
    return render_template("cart.html")

@app.route("/add-to-cart")
def add_to_cart():
    cart = []
    product_id = request.args["product_id"]
    cart.append(product_id)
    flash(f"{Product.get_by_id(product_id).name} has been added")
    return redirect ("/cart")
    


# missing routes:
#   /add-to-cart
#   /clear-cart   [in further study]