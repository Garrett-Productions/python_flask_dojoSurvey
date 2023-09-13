from flask import Flask, render_template,request,redirect,session
app = Flask(__name__)
app.secret_key = "shredthegnarrrrrrr"


@app.route('/')
def hello_world():
    print(request.form)
    return render_template("index.html") #im displaying thigns w render_template


@app.route('/process', methods=["POST"])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(request.form['name'])
    return redirect("/results")


@app.route('/results')
def results():
    return render_template("results.html")


@app.route("/terminate_session")
def terminate_session():
    session.clear()
    return redirect("/")


if __name__=="__main__":   
    app.run(debug=True, port = 5001)