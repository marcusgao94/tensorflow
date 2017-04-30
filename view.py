import scipy.io
import matplotlib.pyplot as plt
import numpy as np

data = np.fromfile('/tmp/cifar10_data/cifar-10-batches-bin/data_batch_1.bin', np.uint8)
data = data.reshape(10000, 3073)
for i in range(10000):
    image = data[i][1:].reshape(3, 32, 32)
    image = np.transpose(image, [1, 2, 0])
    label = data[i][0]
    print label
    plt.imshow(image)
    plt.show()

