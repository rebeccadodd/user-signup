from flask import Flask, request, render_template

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=["POST"])
def sign_up():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']
    #We got the info from the form submitted by the user
    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "" or " " in username or len(username) < 3 or len(username) > 20:
        username_error = "Invalid username"

    if password == "" or " " in password or len(password) < 3 or len(password) > 20:
        password_error = "Invalid password"

    if verify == "" or verify != password:
        verify_error = "Your passwords do not match"

    if email != "":
        if "@" not in email or "." not in email or " " in email or len(email) < 3 or len(email) > 20:
            email_error = "Invalid email"

    if email_error == "" and username_error == "" and verify_error == "" and password_error == "":
        return render_template("welcome.html", username = username)  
    else:
        return render_template("index.html", username_error = username_error
                                           , password_error = password_error
                                           , verify_error = verify_error
                                           , email_error = email_error
                                           , username = username
                                           , email = email)  

@app.route("/")
def index():
    return render_template("index.html")

app.run()
