import joblib

loaded_model = joblib.load("./Models/iris_log_reg.pkl")
class model():

    def predict(prediction):
        mapping = {
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }
        return mapping.get(prediction, 'Prediction inconnue')
