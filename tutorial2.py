from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is home page"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# redirect to a specific page
# also using this /admin/ we can go to admin/ too but without addressing 
# it like this we won't be able to do that 
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))

if __name__ == "__main__":
    app.run()