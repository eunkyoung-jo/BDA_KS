#2018/11
import numpy as np
import matplotlib.pyplot as plt

def prepare_data(num_points, a, b):
    d_vector = []
    for i in range(num_points):
        x = np.random.normal(0.0, 0.5)
        y = x * a + np.random.normal(0.0, 0.03) * b
        # fill here
    print(d_vector)
    # fill here


    return x_data, y_data

if __name__ == "__main__":
    x_data, y_data = prepare_data(100, 0.1, 0.3)
    plt.plot(x_data, y_data, 'bo', label='Original data')
    plt.legend()
    plt.show()

