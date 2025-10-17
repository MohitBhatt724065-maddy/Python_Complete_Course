# Using Nested loop.
value = [(x,y) for x in range(5) for y in range(5)]
print(value)

# Extracting x and y from value.
x_cord = [x for x , y in value]
y_cord = [y for x, y in value]
print(x_cord)
print(y_cord)

# Visualization using scatter and line plot using matplotlib.
import matplotlib.pyplot as plt

plt.scatter(x_cord, y_cord)
plt.plot(x_cord, y_cord)
plt.show()