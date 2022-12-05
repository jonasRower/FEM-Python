import numpy as np


E = 30
my = 0.25
t = 0.5

b = 3
h = 2

# Matice D
D0 = E/(1-my*my)
D = [[D0, my*D0, 0], [my*D0, D0, 0], [0, 0, D0*(1-my)/2]]


def vratMaticiTuhostiElementu(b, h, D):

    # Element 1
    x12 = 0
    y12 = -h
    x13 = b
    y13 = 0
    x23 = b
    y23 = h

    x21 = -x12
    y21 = -y12
    y31 = -x13
    y31 = -y13
    x32 = -x23
    y32 = -y23


    detJ = x13*y23 - x23*y13

    B = [[y23, 0, y31, 0, y12, 0], [0, x32, 0, x13, 0, x21], [x32, y23, x13, y31, x21, y12]]
    B = np.multiply(B, 1/detJ)
    BT = np.transpose(B)
    BTD = np.matmul(BT, D)
    BTDB = np.matmul(BTD, B)
    K = np.multiply(BTDB, t*detJ/2)


    print(K)


vratMaticiTuhostiElementu(b, h, D)