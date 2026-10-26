import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

X = np.array([
    [0, 0, 1],
    [1, 1, 1],
    [1, 0, 1],
    [0, 1, 1]
])
y = np.array([[0], [1], [1], [0]])

np.random.seed(42)
weights = 2 * np.random.random((3, 1)) - 1

for _ in range(10000):
    input_layer = X
    outputs = sigmoid(np.dot(input_layer, weights))
    error = y - outputs
    adjustments = error * sigmoid_derivative(outputs)
    weights += np.dot(input_layer.T, adjustments)

new_patient = np.array([1, 0, 0])
pred = sigmoid(np.dot(new_patient, weights))
print("Trained Predictions:", np.round(outputs.flatten(), 3))
print("New Patient Disease Probability:", round(float(pred[0]), 4))
print("Diagnosis:", "Positive" if pred[0] >= 0.5 else "Negative")
