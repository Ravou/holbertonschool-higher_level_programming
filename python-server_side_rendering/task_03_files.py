from flask import Flask, render_template, request
import json
import csv
import os

app = Flask(__name__)

def read_json_file(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        return []

def read_csv_file(filename):
    data = []
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert id to int and price to float
                try:
                    row['id'] = int(row['id'])
                    row['price'] = float(row['price'])
                except:
                    pass
                data.append(row)
    except Exception as e:
        pass
    return data

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    error = None
    products = []

    # Read data
    if source == "json":
        products = read_json_file('products.json')
    elif source == "csv":
        products = read_csv_file('products.csv')
    else:
        error = "Wrong source"
        return render_template("product_display.html", error=error)

    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products if int(p['id']) == product_id]
            if not filtered:
                error = "Product not found"
            products = filtered
        except ValueError:
            error = "Invalid ID format"

    return render_template("product_display.html", products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

