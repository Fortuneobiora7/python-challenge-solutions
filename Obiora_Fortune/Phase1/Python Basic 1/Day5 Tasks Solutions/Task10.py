'''
10. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
'''

x1, y1 = 4, 0
x2, y2 = 6, 6
result = ((((x1 - x2)**2) + ((y1 - y2)**2)))**0.5
print(result)

#or better still....
import math
point1 = [4, 0]
point2 = [6, 6]
distance_between = math.sqrt(((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2))
print(round(distance_between, 3))