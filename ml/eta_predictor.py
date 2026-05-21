class ETAPredictor:
    def __init__(self, model):

        self.model = model

    def estimate(self, distance, hour, traffic, weather):

        return self.model.predict_eta(distance, hour, traffic, weather)
