from flask import Flask, render_template

app=Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/tableau')
def tableau():
    return render_template("tableau.html")
@app.route('/education')
def education():
    return render_template("education.html")

@app.route('/experience')
def experience():
    return render_template("experience.html")

if __name__ == '__main__':
    app.run()
