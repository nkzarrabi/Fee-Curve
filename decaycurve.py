import numpy as np
import matplotlib.pyplot as plt

# Adjust the function to ensure y = 0 at x = 1000
def calculate_y(x, b=-0.0034):
    # For x < 200, y = 1 (constant)
    # For 200 <= x < 1000, apply the exponential decay
    # At x = 1000, ensure y = 0
    return np.where(x < 1, 1, np.where(x <= 1000, np.exp(b * (x)), 0))

# Generate x values from 0 to 1 billion (inclusive)
x_values = np.linspace(0, 1000, 1001)  # From 0 to 1 billion tokens

# Calculate y values using the modified function
y_values = calculate_y(x_values)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='Discount Rate vs. Token Supply')
plt.title('Discount Rate vs. Token Supply')
plt.xlabel('Token Supply (in millions)')
plt.ylabel('Discount Rate (normalized)')
plt.fill_between(x_values, y_values, alpha=0.1)  # Optional: Fill under curve
plt.ylim(0, 1)  # Ensure y-axis is limited to [0, 1]
plt.xlim(0, 1000)  # x-axis limits to show full range
plt.grid(True)
plt.legend()
plt.savefig('decay_curve.png') 
plt.show()

# Save the plot to a file

