import os
import numpy as np
dir = '/tmp/cifar10_data/cifar-10-batches-bin'
files = []
for i in range(1, 6):
    files.append(os.path.join(dir, 'data_batch_%d.bin' % i))
files.append(os.path.join('test_batch.bin'))
fout = open('test.bin', 'w')
hold = [1, 3, 8]
for f in files:
    fin = open(f, 'rb')
    data = np.fromfile(fin, np.uint8)
    data = data.reshape(10000, 3073)
    for i in range(10000):
        label = data[i][0]
        if (label not in hold):
            continue
        

