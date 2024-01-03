import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input data
inputs = np.array([[0, 0],
                    [0, 1],
                    [1, 0],
                    [1, 1]])

# Output data
outputs = np.array([[0], [1], [1], [0]])

# Seed for reproducibility
np.random.seed(42)

# Initialize weights
input_dim = inputs.shape[1]
hidden_dim = 4
output_dim = 1

weights_input_hidden = np.random.uniform(size=(input_dim, hidden_dim))
weights_hidden_output = np.random.uniform(size=(hidden_dim, output_dim))

# Training
epochs = 10000
learning_rate = 0.1

for epoch in range(epochs):
    # Forward pass
    hidden_layer_input = np.dot(inputs, weights_input_hidden)
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output)
    predicted_output = sigmoid(output_layer_input)

    # Backpropagation
    error = outputs - predicted_output
    output_delta = error * sigmoid_derivative(predicted_output)

    hidden_layer_error = output_delta.dot(weights_hidden_output.T)
    hidden_layer_delta = hidden_layer_error * sigmoid_derivative(hidden_layer_output)

    # Update weights
    weights_hidden_output += hidden_layer_output.T.dot(output_delta) * learning_rate
    weights_input_hidden += inputs.T.dot(hidden_layer_delta) * learning_rate

# Testing
new_inputs = np.array([[0, 0],
                       [0, 1],
                       [1, 0],
                       [1, 1]])

hidden_layer_output = sigmoid(np.dot(new_inputs, weights_input_hidden))
predicted_output = sigmoid(np.dot(hidden_layer_output, weights_hidden_output))

print("Predicted Output:")
print(predicted_output)
