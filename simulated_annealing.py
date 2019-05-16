import numpy as np
import matplotlib.pyplot as plt

'''
find the minimum point by using simulated annealing method
'''


def obj_function(x):
    y = x ** 3 - 60 * x ** 2 - 4 * x + 6
    return y


# plot
# x = np.linspace(0, 100, 1000)
# y = obj_function(x)
# plt.plot(x, y)
# plt.show()


if __name__ == '__main__':
    T = 1000    # initiate temperature
    Tmin = 10   # minimum temperature
    x = np.random.uniform(low=0, high=100)
    k = 50  # iterations of internal circulation
    y = 0   # initiate result
    t = 0   # iteration of outer circulation
    delta = 0.99    # decay rate

    while T > Tmin:
        for i in range(k):
            y = obj_function(x)
            # generate a new x (core part)
            xNew = x + np.random.uniform(low=-0.055, high=0.055) * T
            if 0 <= xNew <= 100:
                yNew = obj_function(xNew)
                if yNew < y:
                    x = xNew
                else:
                    p = np.exp(-(yNew - y) / T)     # acceptable rate
                    r = np.random.uniform(low=0, high=1)
                    # if acceptable rate bigger than a random number, accept it
                    if p > r:
                        x = xNew

        t += 1
        T *= delta
        print('No. %d: x = %f, y = %f' % (t, x, y))




