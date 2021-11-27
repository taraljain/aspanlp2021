from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def NLP():
    if request.method == "POST":
        sentence = request.form["sentence"]

        # Find the sentiment using our NLP Project and display
        return render_template('index.html', sentence = sentence)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
