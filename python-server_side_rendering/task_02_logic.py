from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    # Path to JSON file
    json_path = os.path.join(os.path.dirname(__file__), 'items.json')
    
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
            items = data.get('items', [])
    except Exception as e:
        items = []
        print(f"Error reading items.json: {e}")

    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

