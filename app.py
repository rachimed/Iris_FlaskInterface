from flask import Flask, render_template, request,  url_for, redirect
import pandas as pd
from Models.models import model

# instanciation off app Flask
app = Flask(__name__)


#! Routes
@app.route("/")
def home():


    return render_template('index.html')

#! Route formulaire

@app.route('/form', methods=["POST", "GET"])
def form():
    
    
    if request.method == 'POST':
        data = {}
        
        sepal_length= float(request.form['sepal length'])
        sepal_width= float(request.form['sepal width'])
        petal_length= float(request.form['petal length'])
        petal_width = float(request.form['petal width'])
        
        data={
            'sepal length':sepal_length,
            'sepal width':sepal_width,
            'petal length':petal_length,
            'petal width':petal_width,
        }
        # photo={
        #     0: "./static/stock-photo-iris-setosa-is-a-perennial-plant-with-blue-flowers-2317812741.jpg",
        #     1:"./static/versicolor.jpg",
        #     2:"./static/virginica.jpg"
        # }
        # image= photo['']
        
        df = pd.DataFrame(data, index=[0])
        
        result = model.predict(df)
        
        print(sepal_length, sepal_width, petal_length, petal_width)
        
        return render_template('form.html', result=result, title="identification")
    else:
        return render_template('form.html', title="identification")

# Variables environement
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0',port=8080)