from flask import Flask, render_template, request
from pickle import load
from util import proba_to_res

app = Flask(__name__)
model = None


@app.route("/")
def index_page():
    return get_prediction("Today I have had an amazing day")


@app.route("/get_prediction", methods=["GET", "POST"])
def get_prediction(text=""):
    if request.method == "POST":
        text = request.form['text']
    prediction_prob = model.predict_proba([text])[0][1]
    return render_template('index.html', text=text, result=proba_to_res(prediction_prob, model.best_threshold),
                           prediction_prob=f'{prediction_prob:.2f}')


if __name__ == "__main__":
    with open("model.pkl", 'rb') as file:
        model = load(file)
    app.run(debug=True)
