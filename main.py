#from stat import IO_REPARSE_TAG_APPEXECLINK
from flask import Flask, render_template
from prototype_backend import *

app = Flask(__name__)

@app.route("/")
def index(): 
    my_string = "hell world"

    # Call to prototype_backend.py to calculate reutrn from search input
    track_uri = get_results()

    #album_uri = 'spotify:album:0f4TeyGJMm9iLjD38er2lO'.split(':')[-1]
    # Hook up to prototype_backend.py so that track_uri is fetched on the backend
    #track_uri = 'spotify:track:1elJ0Y0i1ZxzpbuLgK3YTO'.split(':')[-1]
    
    return render_template("index.html", body=my_string, uri=track_uri)

if __name__ == "__main__":
    app.run()