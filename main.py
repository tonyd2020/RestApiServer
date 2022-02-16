import json

from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/products/popular')
def popular():
    return json.dumps({

    })

app.run()