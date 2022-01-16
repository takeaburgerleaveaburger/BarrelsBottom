from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")

def index(): 
    my_string = "hello world"
    return render_template("index.html", body=my_string)

if __name__ == "__main__":
    app.run()