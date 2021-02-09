from flask import Flask, flash, request, render_template, redirect, url_for

from form import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardsecretkey'


@app.route("/")
def Index():
    context = {
        'text': "This is data by index",
        'name': 'Bob'
    }

    return render_template("index.html", data=context)


@app.route('/contact')
def Contact():
    return render_template("contact.html")


@app.route('/about')
def About():
    return render_template("about.html")


@app.route('/login', methods=['GET', 'POST'])
def Login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form['username'] != 'Mateusz' or request.form['password'] != '123':
            print("Dobry login")
            flash("Invalid Credntials, Please try Again")
        else:
            return redirect(url_for('Index'))
            print("Zły login")

    return render_template("login.html", title='Login', form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


@app.errorhandler(500)
def internal_serwer_error(e):
    return render_template('500.html')


if __name__ == "__main__":
    app.run(debug=True)

"""


<div class ="alert alert-success alert-dismissable" role="alert">
 <button type="button" class="close" data-dismiss="alert" aria-label="Close">
    <span aria-hidden="true">X</span>



         </button>

         {{message}}
    </div>



def Login():
    form = LoginForm()

    if form.validate_on_submit():
        return  redirect(url_for('Index'))

    print(form.errors)
    print("done")
    return render_template("login.html", title='Login', form=form)


@app.route('/set')
def setCookie():
    response = make_response("i have have set the cookie")
    response.set_cookie("main", "Flask Web Development")

    return response

@app.route("/get")
def getCookie():
    myapp = request.cookies.get("main")
    return "Cookie Content is" + str(myapp)

@app.route('/user/<name>')
def User(name):
    return "<h1> Welcome Mr. {} </h1>".format(name)


"""
