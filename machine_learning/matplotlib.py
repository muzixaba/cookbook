#=====================
# Imports
#=====================
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

#====================
# Line Graph
#====================
data = {'a': 1, 'b': 2, 'c': 3}
x_values = list(data.keys())
y_values = list(data.values())
plt.plot(x_values, y_values, color='red', alpha=0.5)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Graph Title \n Subtitle')
plt.show()

#==================
# Bar Graph
#==================
data = {'a': 1, 'b': 2, 'c': 3}
x_values = list(data.keys())
y_values = list(data.values())
plt.bar(x_values, y_values)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Graph Title \n Subtitle')
plt.show()

#==================
# Scatter Plot
#==================
# Shows relationship between two variables
# Great for checking corralation
x_values = [np.random.randint(10) for i in range(10)]
y_values = [np.random.randint(10) for i in range(10)]
plt.scatter(x_values, y_values)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Graph Title \n Subtitle')
plt.show()

#==================
# Pie Chart
#==================
# Shows proportion/share each category has within the total.
data = {'a': 1, 'b': 2, 'c': 3}
x_values = list(data.keys())
y_values = list(data.values())
plt.pie(y_values, labels=x_values, autopct='%1.1f%%')
plt.title('Pie Chart \n Subtitle')
plt.show()

#=======================
# View images from files
#=======================
img2 = mpimg.imread('/path/to/image.png')
plt.imshow(img2)

#===================
# Set Style
#===================
plt.style.use('ggplot')
