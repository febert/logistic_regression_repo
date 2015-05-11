import cPickle, gzip, numpy
import theano.tensor as T
import theano

# Load the dataset
f = gzip.open('mnist.pkl.gz', 'rb')
train_set, valid_set, test_set = cPickle.load(f)

def shared_dataset(data_xy):

    data_x, data_y = data_xy
    shared_x = theano.shared(numpy.asarray(data_x, dtype=theano.config.floatX))
    shared_y = theano.shared(numpy.asarray(data_y, dtype=theano.config.floatX))

    return shared_x, T.cast(shared_y, 'int32')


test_set_x, test_set_y = shared_dataset(test_set)
valid_set_x, valid_set_y = shared_dataset(valid_set)
train_set_x, train_set_y = shared_dataset(train_set)

batch_size = 500    # size of the minibatch ; 20 ??

# accessing the third minibatch of the training set

data  = train_set_x[2 * 500: 3 * 500]
label = train_set_y[2 * 500: 3 * 500]


import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

pic1=test_set_x.get_value()[24].reshape((28,28))
print pic1.shape
print train_set[0].shape

plt.imshow(pic1, cmap = cm.Greys_r, interpolation= 'none')
plt.show()
#print test_set[0][0]


f.close()

