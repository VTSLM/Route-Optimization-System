import joblib


model = joblib.load("ml/eta_model.pkl")


def predict_eta(distance_km, hour, day_of_week, traffic_level):

    prediction = model.predict([[distance_km, hour, day_of_week, traffic_level]])

    return prediction[0]
