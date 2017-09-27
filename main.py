from utils import to_categorical_4d
from model import FCN8
import tensorflow as tf
import numpy as np
import ear_pen

if __name__ == '__main__':
    """
    (train_img, train_ann), (test_img, test_ann) = ear_pen.load_data()
    train_ann = np.asarray(train_ann) / 256
    train_ann, _map = to_categorical_4d(train_ann)
    """

    img_ph = tf.placeholder(tf.float32, [None, 1040, 780, 3])
    ann_ph = tf.placeholder(tf.float32, [None, 1040, 780, 3])
    net = FCN8(img_ph, ann_ph)

    print(net.loss, net.optimize)

    """
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        for i in range(1):
            feed_dict = {
                img_ph: train_img[0:2],
                ann_ph: train_ann[0:2]
            }
            _loss = sess.run(net.loss, feed_dict=feed_dict)
            print('iter: ', i, '\tloss: ', _loss)
    """