from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def NLP():
    if request.method == "POST":
        print(request.form["sentence"])

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)