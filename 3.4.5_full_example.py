import tensorflow as tf


from numpy.random import RandomState

batch_size=8

w1=tf.Variable(tf.random_normal([2,3],stddev=1,seed=1))
w2=tf.Variable(tf.random_normal([3,1],stddev=1,seed=1))

x= tf.placeholder(tf.float32,shape=(None,2),name='x-input')
y_=tf.placeholder(tf.float32,shape=(None,2),name='y-input')


# 前向传播算法
a=tf.matmul(x,w1)
y=tf.matmul(a,w2)

# 损失函数和反向传播算法
y=tf.sigmoid(y)
cross_entropy=-tf.reduce_mean(
    y_*tf.log(tf.clip_by_value(y,1e-10,1.0))
    +(1-y)*tf.log(tf.clip_by_value(1-y,1e-10,1.0))
)

train_step=tf.train.AdamOptimizer(0.001).minimize(cross_entropy)


rdm=RandomState(1)
dataset_size=128
X=rdm.rand(dataset_size,2)


Y=[[int(x1+x2<1)] for (x1,x2) in X]


with tf.Session() as sess:
    init_op=tf.global_variables_initializer()
    sess.run(init_op)

    print( sess.run(w1))
    print( sess.run(w2))

    w1=[[]]

