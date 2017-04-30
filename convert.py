import os
import numpy as np
import cifar10

dir = '../cifar10/cifar-10-batches-bin'
files = []
for i in range(1, 6):
    files.append(os.path.join(dir, 'data_batch_%d.bin' % i))
files.append(os.path.join(dir, 'test_batch.bin'))
hold = [1, 3, 8]
res = []
for f in files:
    print f
    fin = open(f, 'rb')
    data = np.fromfile(fin, np.uint8)
    data = data.reshape(10000, 3073)
    for i in range(10000):
        label = data[i][0]
        if (label not in hold):
            continue
        res.append(data[i])
    fin.close()
fout = open('test.bin', 'wb')
res = np.array(res, dtype=np.uint8)
res.tofile(fout)
fout.close()

