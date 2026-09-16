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

#==================================================================
#next graph
#==================================================================

print("=================NEXT GRAPH===============")

a = [1, 2, 3, 4, 5]
b = [0, 0.6, 0.2, 15, 10, 8, 16, 21]
c = [4, 2, 6, 8, 3, 20, 13, 15]

fig = plt.figure(figsize =(10, 10))

sub1 = plt.subplot(2, 2, 1)
sub2 = plt.subplot(2, 2, 2)
sub3 = plt.subplot(2, 2, 3)
sub4 = plt.subplot(2, 2, 4)

sub1.plot(a, 'sb')

sub1.set_xticks(list(range(0, 10, 1)))
sub1.set_title('1st Rep')

sub2.plot(b, 'or')

sub2.set_xticks(list(range(0, 10, 2)))
sub2.set_title('2nd Rep')

sub3.plot(list(range(0, 22, 3)), 'vg')
sub3.set_xticks(list(range(0, 10, 1)))
sub3.set_title('3rd Rep')

sub4.plot(c, 'Dm')

sub4.set_yticks(list(range(0, 24, 2)))
sub4.set_title('4th Rep')

plt.show()