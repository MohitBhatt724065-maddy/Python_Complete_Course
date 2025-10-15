# Using list comprehension and nested loop to generate values.
value = [(cord_x, cord_y) for cord_x in range(10) for cord_y in range (10)]
print(value)

import matplotlib.pyplot as plt

x_value = cord_x
y_value = cord_y
plt.plot(x_value, y_value, s=100)
plt.show