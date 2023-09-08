import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def generate_data(size=100):
    np.random.seed(0)
    X = 2 * np.random.rand(size, 1)
    y = 4 + 3 * X + np.random.randn(size, 1)
    return X, y


def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return mse


def main():
    # Take input from user for the number of data points
    data_size = int(input("Enter the number of data points you want to generate (default is 100): ") or "100")

    X, y = generate_data(data_size)
    model, X_test, y_test = train_model(X, y)
    mse = evaluate_model(model, X_test, y_test)

    print(f"Mean Squared Error: {mse:.2f}")
    new_data = np.array([[1.5]])
    predicted_value = model.predict(new_data)
    print(f"Predicted value for input {new_data[0][0]} is {predicted_value[0][0]:.2f}")


if __name__ == "__main__":
    main()
