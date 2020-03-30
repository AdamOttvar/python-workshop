#!python3
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib is a module for plotting in python, with a syntax
# that is very similar to how you would plot in Matlab

A simple plot with title, labels and legend
x_values = [i for i in range(21)]
y_values1 = [i for i in range(0, 210, 10)]
y_values2 = [y+5 for y in y_values1]

plt.plot(x_values,y_values1)
plt.plot(x_values,y_values2)
plt.title('Example plot')
plt.ylabel('y-label')
plt.xlabel('x-label')
plt.legend(['A first line', 'A second line'])
plt.show()

# A subplot wiht muliple plots
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[0, 1].set_xlabel('x-label')
axs[0, 1].set_ylabel('y-label')
axs[1, 1].hist2d(data[0], data[1])
fig.suptitle('Example with subplots')
plt.show()
