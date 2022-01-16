from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def index(): 
    my_string = "hell world"
    album_uri = 'spotify:album:0f4TeyGJMm9iLjD38er2lO'.split(':')[-1]
    track_uri = 'spotify:track:1elJ0Y0i1ZxzpbuLgK3YTO'.split(':')[-1]
    return render_template("index.html", body=my_string, uri=track_uri)

if __name__ == "__main__":
    app.run()