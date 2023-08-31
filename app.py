from flask import Flask, render_template, request
import pickle
import json
import numpy as np

with open("model.pkl", "rb") as model_file:
    loaded_model = pickle.load(model_file)

app = Flask(__name__)

@app.route('/',  methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        gender = int(request.form['gender'])
        sscp = int(request.form['sscp'])
        sscb = int(request.form['sscb'])
        hscp = int(request.form['hscp'])
        hscb = int(request.form['hscb'])
        hsca = int(request.form['hsca'])
        hscs = int(request.form['hscs'])
        degp = int(request.form['degp'])
        degts = int(request.form['degts'])
        degto = int(request.form['degto'])
        wex = int(request.form['wex'])
        etest = int(request.form['etest'])
        specs = int(request.form['specs'])
        mbap = int(request.form['mbap'] )

        input_list = [[gender, sscp, sscb, hscp, hscb, degp, wex, etest, specs, mbap, hsca, hscs, degto, degts]]

        prediction = loaded_model.predict(input_list)
        prediction = prediction[0]
        int64_value = np.int64(prediction)
        python_integer = int(int64_value)

        if python_integer == 1 :
            return render_template('P.html')
        else:
            return render_template('NP.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)