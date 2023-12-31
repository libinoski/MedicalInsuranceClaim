from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__, template_folder='./templates', static_folder='./static')

Pkl_Filename = "rf_tuned.pkl" 
with open(Pkl_Filename, 'rb') as file:  
    model = pickle.load(file)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        features = [int(x) for x in request.form.values()]
        final = np.array(features).reshape((1, 6))
        pred = model.predict(final)[0]
        
        if pred < 0:
            return render_template('op.html', pred='Error calculating Amount!')
        else:
            return render_template('op.html', pred=f'₹ {pred:.3f}')
    else:
        # Handle GET requests to '/predict' (e.g., page reload)
        return render_template('home.html')  # You can return a different template or response as needed

# Define the "about" route
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=1234)
