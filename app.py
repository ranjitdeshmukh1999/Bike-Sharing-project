import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open(r'C:\Users\hp\Downloads\trial-main\trial-main\model_pickle', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)

    output = (round(prediction[0], 1))
    return render_template('index.html', prediction_text='Rental Bike Share Prediction is {}'.format(int(output)))
    
 
        

if __name__ == "__main__":
    app.run(debug=True)
    
