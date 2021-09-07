import csv
import matplotlib.pyplot as plt
x_axis = []
y_axis = []
with open('dataset1.csv') as dataset:
    reader = csv.reader(dataset, delimiter=',')
    line_count = 0
    for row in reader:
        if (line_count == 0):
            line_count+=1
        else:
            line_count+=1
            x_axis.append(float(row[0]))
            y_axis.append(float(row[1]))

plt.plot(x_axis, y_axis, 'bo')
plt.show()
