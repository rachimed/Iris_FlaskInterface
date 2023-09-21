import joblib

loaded_model = joblib.load("./Models/iris_log_reg.pkl")
class model():

    def predict(data):
        prediction = loaded_model.predict(data)
        photo={
            0: "./static/stock-photo-iris-setosa-is-a-perennial-plant-with-blue-flowers-2317812741.jpg",
            1:"./static/versicolor.jpg",
            2:"./static/virginica.jpg",
            "nom": "setosa"
        }   
        # image= photo['']
        # mapping = {
        # 0: 'setosa',
        # 1: 'versicolor',
        # 2: 'virginica'
        # }
        # return mapping.get(prediction, 'Prediction inconnue')
        print(loaded_model.predict_proba(data))
        if prediction == 0:
            return  photo[0,"nom"]
        elif prediction == 1:
            return photo[1]
        elif prediction == 2:
            return photo[2]
        else:
            return 'Prediction inconnue'