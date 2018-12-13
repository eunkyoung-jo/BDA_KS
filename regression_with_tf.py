#2018/11
from represent_data import prepare_data
import matplotlib.pyplot as plt
import tensorflow as tf

def regress(x_data, y_data):
    W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
    b = tf.Variable(tf.zeros([1]))
    y = W * x_data + b #y is the estimated, y_data is the real/observed

    loss = tf.reduce_mean(tf.square(y - y_data))
    optimizer = tf.train.GradientDescentOptimizer(0.5)
    train = optimizer.minimize(loss)

    init = tf.global_variables_initializer()

    sess = tf.Session()
    sess.run(init)

    for step in range(101):
        sess.run(train)
        if step % 10 == 0:
            print(step, 'W =', sess.run(W), 'b =', sess.run(b))

    return sess, W, b

# observed/real/original data
x_data, y_data = prepare_data(100, 0.1, 0.3)
# regression
sess, W, b = regress(x_data, y_data)
# visulise
plt.plot(x_data, y_data, 'ro', label='Original_data')
plt.plot(x_data, sess.run(W) * x_data + sess.run(b), label='Linear Regression')
plt.legend()
plt.show()

