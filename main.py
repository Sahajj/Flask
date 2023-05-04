#importing flask from Flask
# redirect is to redirect a user from a page 
# url_for is to direct it to a url "_"

from flask import Flask, redirect, url_for

# this is an instace of a flask web app 
app = Flask(__name__)


# this is the home page or the main page of the web app
# and to access this page we need a address
# To do this we decorate the function with the file address 
@app.route("/")
def home():
    # we can just return some inline html
    return "<h1>Hello! this is the main page</h1> <p>HEllo </p>"


@app.route("/contact")
def contact():
    return f"Hello you can contant me here :) !"


# some cool things that we can do here is 
#  ("/<>") --> it means if i type something this will grab that value and pass it 
# too our function 
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


# this is our admin page routing 
@app.route("/admin")
def admin():
    # now to redirect we directly use redirect and after that we use
    # url_for to get it to where ever we want
    # aslo we need to give the function name not the page name :)
    return redirect(url_for("contact"))


# running the web app  (this will get a website running)
if __name__ == "__main__":
    app.run()