import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#A simple graph markdown

x = [1,2,3,4,5]
y = [1,2,3,4,5]

plt.plot(x,y)

plt.xlabel('X-axix')
plt.ylabel("Y-axis")
plt.title("Sample seetha graph")

plt.show()


#==================================================================
#next graph
#==================================================================

print("=================NEXT GRAPH===============")

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 20, 15, 10, 5]

plt.plot(x, y1, label='y = x^2', color='green', linestyle='--', marker='o')
plt.plot(x, y2, label='y = 30 - x^2', color='red', linestyle='-', marker='x')

plt.grid(True)

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Customized Line Plot with Multiple Series')

plt.legend()
plt.savefig('all_features_plot.png')
plt.show()