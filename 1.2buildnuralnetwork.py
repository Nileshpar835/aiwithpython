import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# =========================
# DATA
# =========================
distance = torch.tensor([[1.0],[2.0],[3.0],[4.0],[5.0]], dtype=torch.float32)
times = torch.tensor([[6.96],[12.11],[16.77],[22.21],[27.74]], dtype=torch.float32)

# =========================
# MODEL
# =========================
model = nn.Linear(1, 1)

# =========================
# LOSS & OPTIMIZER
# =========================
loss_function = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# =========================
# TRAINING
# =========================
for epoch in range(500):
    optimizer.zero_grad()
    output = model(distance)
    loss = loss_function(output, times)
    loss.backward()
    optimizer.step()

    if epoch % 50 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

# =========================
# TEST
# =========================
with torch.no_grad():
    test_distance = torch.tensor([[6.0]], dtype=torch.float32)
    predicted_time = model(test_distance)
    print(f"\nPrediction: {predicted_time.item():.2f} minutes")

# =========================
# PARAMETERS
# =========================
print("\nLearned Parameters:")
for name, param in model.named_parameters():
    print(name, param.data)

# =========================
# PLOTTING FUNCTIONS
# =========================
def plot_results(model, distances, times):
    model.eval()
    with torch.no_grad():
        predicted_times = model(distances)

    plt.figure()
    plt.plot(distances.numpy(), times.numpy(), marker='o', linestyle='None', label='Actual')
    plt.plot(distances.numpy(), predicted_times.numpy(), label='Prediction')
    plt.title('Actual vs Predicted')
    plt.xlabel('Distance')
    plt.ylabel('Time')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_nonlinear_comparison(model):
    new_distances = torch.tensor([[1.0],[2.0],[3.0],[4.0],[5.0]], dtype=torch.float32)
    new_times = torch.tensor([[5.0],[9.0],[15.0],[25.0],[40.0]], dtype=torch.float32)

    model.eval()
    with torch.no_grad():
        predictions = model(new_distances)

    plt.figure()
    plt.plot(new_distances.numpy(), new_times.numpy(), marker='o', linestyle='None', label='Non-linear Data')
    plt.plot(new_distances.numpy(), predictions.numpy(), label='Linear Model')
    plt.title('Linear Model vs Non-linear Data')
    plt.xlabel('Distance')
    plt.ylabel('Time')
    plt.legend()
    plt.grid(True)
    plt.show()

# =========================
# CALL FUNCTIONS (IMPORTANT)
# =========================
plot_results(model, distance, times)
plot_nonlinear_comparison(model)