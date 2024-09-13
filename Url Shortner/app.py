# handle shorting of the url that was sent from database.py
from flask import Flask, render_template, g
from database import handle
import pyshorteners
from pyshorteners import Shortener

app = Flask(__name__)
@app.route('/', methods=["GET", "POST"])
def index():
    new_url = "Your new url"
    old_url = "Enter The Url You Would Like To Short"
    handle()
    if hasattr(g, 'url_handle'): 
        old_url = g.url_handle 
        s = pyshorteners.Shortener()
        new_url = s.tinyurl.short(g.url_handle)
    else:
        print("OOF")

    return render_template('index.html', new_url=new_url, old_url=old_url)  
        


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)

