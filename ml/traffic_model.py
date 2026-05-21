from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error


class TrafficModel:
    def __init__(self):

        self.model = RandomForestRegressor()

    def train(self, dataframe):

        X = dataframe[["distance", "hour", "traffic_level", "weather"]]

        y = dataframe["eta"]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        self.model.fit(X_train, y_train)

        predictions = self.model.predict(X_test)

        error = mean_absolute_error(y_test, predictions)

        print(f"Mean Absolute Error: {error:.2f}")

    def predict_eta(self, distance, hour, traffic_level, weather):

        prediction = self.model.predict([[distance, hour, traffic_level, weather]])

        return prediction[0]
