from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("/../../frontend/index.html")

@app.route("/login", methods=['POST'])
def login():
    if request.method=='POST':
        email = request.form["email_name"]
        password = request.form["password_name"]
        print(email,password)
        return render_template("/../../frontend/login.html")

'''@app.route("/signin")
def signin()
    return render_template("/../../frontend/signin.html")

@app.route("/verification")
def verification()
    return render_template("/../../frontend/verification.html")

@app.route("/hub")
def hub()
    return render_template("/../../frontend/verification.html")'''


if __name__ == '__main__':
    app.debug=True
    app.run()