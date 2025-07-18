from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

def read_json_file(filename):
    try:
        with open(filename) as f:
            data = json.load(f)
        return data.get("items", []) if "items" in data else data
    except Exception:
        return None

def read_csv_file(filename):
    try:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except Exception:
        return None

def read_sqlite_data(filename, item_id=None):
    try:
        conn = sqlite3.connect(filename)
        cursor = conn.cursor()
        if item_id:
            cursor.execute("SELECT id, name, category, price FROM Products WHERE id=?", (item_id,))
            row = cursor.fetchone()
            conn.close()
            return [dict(id=row[0], name=row[1], category=row[2], price=row[3])] if row else []
        else:
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            conn.close()
            return [dict(id=row[0], name=row[1], category=row[2], price=row[3]) for row in rows]
    except Exception:
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    item_id = request.args.get('id', type=int)
    error = None
    data = []

    if source == 'json':
        data = read_json_file('products.json')
        if data is None:
            error = "Error reading JSON file."
    elif source == 'csv':
        data = read_csv_file('products.csv')
        if data is None:
            error = "Error reading CSV file."
    elif source == 'sql':
        data = read_sqlite_data('products.db', item_id)
        if data is None:
            error = "Database error or product not found."
        elif item_id and not data:
            error = "Product not found."
    else:
        error = "Wrong source."

    return render_template("product_display.html", products=data, error=error)

if __name__ == "__main__":
    app.run(debug=True)

