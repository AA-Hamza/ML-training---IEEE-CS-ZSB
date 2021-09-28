import random
import csv
import matplotlib.pyplot as plt

points = {} 
m = 0
with open('dataset.csv') as dataset:
    reader = csv.reader(dataset, delimiter=",")
    next(reader)    #ignoring header row
    for row in reader:
        points[float(row[0])] = float(row[1])
        m += 1

x_points = list(points.keys())


def hypothesis(x, theta0, theta1):
    return theta0+theta1*x

def cost_function(theta0, theta1):
    sumation = 0;
    for i in range(0, m):
        sumation += (hypothesis(x_points[i], theta0, theta1) - points[x_points[i]])**2
    return (1/(2*m))*sumation

def gradient_descent(theta0, theta1, learning_rate):
    sumation_theta0 = 0
    for i in range(0, m):
        sumation_theta0 += (hypothesis(x_points[i], theta0, theta1) - points[x_points[i]])

    sumation_theta1 = 0
    for i in range(0, m):
        sumation_theta1 += (hypothesis(x_points[i], theta0, theta1) - points[x_points[i]])*x_points[i]

    theta0 = theta0 - learning_rate * (1/m) * sumation_theta0
    theta1 = theta1 - learning_rate * (1/m) * sumation_theta1
    return theta0, theta1


def main():
    theta0 = random.random()
    theta1 = random.random()
    _LEARNING_RATE = 0.0002

    print("Cost\tTheta0\tTheta1")
    print(cost_function(theta0, theta1), theta0, theta1)
    for i in range(100):       #Should check for convergence but it doesn't really matter here
        theta0, theta1 = gradient_descent(theta0, theta1, _LEARNING_RATE)
    print(cost_function(theta0, theta1), theta0, theta1)


    #plotting results
    plt.plot(x_points, points.values(), 'bo', label="Original Dataset")
    x_min, x_max = int(min(x_points)), int(max(x_points))
    x_axis = [x for x in range(x_min, x_max)]
    y_result = [hypothesis(x, theta0, theta1) for x in x_axis]
    plt.plot(x_axis, y_result, label="Trained Line")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

if __name__ == '__main__':
    main()
