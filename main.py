from flask import Flask, request, render_template, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html")

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""

        if (username == ""
                or " " in username
                or len(username) < 3
                or len(username) > 20):
            error_username = "Please enter a valid username"

        if (password == ""
                or " " in password
                or len(password) < 3
                or len(password) > 20):
            error_password = "Please enter a valid password"

        if verify == "":
            error_verify = "Please enter a valid password"

        if verify != password:
            error_verify = "Passwords do not match"

        if email != "":
            if ('@' not in email
                    or "." not in email
                    or " " in email
                    or len(email) < 3
                    or len(email) > 20):
                error_email = "Please enter a valid email address"

        if (error_username == ""
                and error_password == ""
                and error_verify == ""
                and error_email == ""):
            return redirect("/welcome?username=" + username)
        else:
            return render_template("signup.html", error_username=error_username,
                                                  error_password=error_password,
                                                  error_verify=error_verify,
                                                  error_email=error_email,
                                                  username=username,
                                                  email=email)

@app.route("/welcome", methods=['GET'])
def welcome():
    username = request.args.get('username')
    return render_template("welcome.html", username=username)

@app.route("/", methods=['GET'])
def index():
    return redirect("/signup")

if __name__ == '__main__':
    app.run()
